import torch
import torch.nn as nn
import numpy as np
import pandas as pd

import transformers
from transformers import AutoModel, BertTokenizerFast, GPT2TokenizerFast

DEVICE = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

MAX_LENGHT = 65
do_use_bert_large = False
do_use_gpt2_large = False
DROPOUT = .1

class BERT_Arch(nn.Module):
    def __init__(self, bert):  
        super(BERT_Arch, self).__init__()
        self.bert = bert
        self.dropout = nn.Dropout(DROPOUT)
        self.relu =  nn.ReLU()
        if do_use_bert_large:
            self.fc1 = nn.Linear(1024,512)
            self.fc2 = nn.Linear(512,2)
        else:
            self.fc1 = nn.Linear(768,512)
            self.fc2 = nn.Linear(512,2)
        self.softmax = nn.LogSoftmax(dim=1)
    def forward(self, sent_id, mask):
        cls_hs = self.bert(sent_id, attention_mask=mask)['pooler_output']
        x = self.fc1(cls_hs)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x
        
class GPT2_Arch(nn.Module):
    def __init__(self, gpt2):  
        super(GPT2_Arch, self).__init__()
        self.gpt2 = gpt2
        self.dropout = nn.Dropout(DROPOUT)
        self.relu =  nn.ReLU()
        if do_use_gpt2_large:
            self.fc1 = nn.Linear(1024,512)
            self.fc2 = nn.Linear(512,2)
        else:
            self.fc1 = nn.Linear(768,512)
            self.fc2 = nn.Linear(512,2)
        self.softmax = nn.LogSoftmax(dim=1)
    def forward(self, sent_id, mask):
        cls_hs = self.gpt2(sent_id, attention_mask=mask).last_hidden_state[:, 0, :]
        x = self.fc1(cls_hs)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

class FakeNewsDetector:
    def __init__(self, model_name, pre_trained_model, tokenizer, model_path):
        if model_name == "BERT":
            self.model = BERT_Arch(pre_trained_model)
        elif model_name == "GPT2":
            self.model = GPT2_Arch(pre_trained_model)
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
        self.tokenizer = tokenizer

    def __call__(self, text, prob=True):
        if isinstance(text, str):
            text = [text]
            unpack = True
        else:
            unpack = False
            
        # prepare input     
        tokens = self.tokenizer.batch_encode_plus(
            text,
            padding="max_length", 
            max_length=MAX_LENGHT,
            truncation=True
        )
        seq = torch.tensor(tokens['input_ids'])
        mask = torch.tensor(tokens['attention_mask'])
        
        # predict
        logit = self.model(seq, mask)
        
        # get probability of each class
        if prob:
            probs = torch.exp(logit)
            if unpack:
                return probs[0,:].tolist()
            else:
                return probs[:,:].tolist()
        else:
            return logit.argmax(1)

# For LSTM
import torchtext.functional as F
import torchtext.transforms as T
from torch.hub import load_state_dict_from_url
from torch.autograd import Variable
import torch.nn.functional as nnF

class LSTM_Arch(nn.Module):
    def __init__(self, vocab_size, embedding_dim=300, hidden_dim=50, label_size=2,
                 batch_size=1, dropout=0.5, bidirectional=True, classifier_head=None):
        """Prepare individual layers"""
        super(LSTM_Arch, self).__init__()
        self.hidden_dim = hidden_dim
        self.batch_size = batch_size
        self.dropout = dropout
        self.num_directions = 2 if bidirectional else 1
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(input_size=embedding_dim, hidden_size=hidden_dim, bidirectional=bidirectional)
        self.hidden2label = nn.Linear(hidden_dim*self.num_directions, label_size)
        self.hidden = self.init_hidden()
        self.classifier_head = classifier_head

    def init_hidden(self, batch_size=None):
        """Choose appropriate size and type of hidden layer"""
        if not batch_size:
            batch_size = self.batch_size
        #what = torch.randn
        what = torch.zeros
        # first is the hidden h
        # second is the cell c
        return (Variable(what(self.num_directions, batch_size, self.hidden_dim)),
                Variable(what(self.num_directions, batch_size, self.hidden_dim)))

    def classify(self, features):
        y = self.hidden2label(features)
        log_probs = nnF.log_softmax(y, dim=1)
        return log_probs

    def forward(self, sentence):
        """Use the layers of this model to propagate input and return class log probabilities"""
        x = self.embeddings(sentence).permute(1,0,2)
        batch_size = x.shape[1]
        self.hidden = self.init_hidden(batch_size=batch_size)
        lstm_out, self.hidden = self.lstm(x, self.hidden)
        features = lstm_out[-1]
        if self.classifier_head:
            #unsqueeze: introduce dummy second dimension, so that classifier_head can drop it
            return self.classifier_head(torch.unsqueeze(features, 1))
        else:
            return self.classify(features)
            
class LSTMDetector:
    def __init__(self, vocab_size, text_transform, padding_idx, model_path):
        self.model = LSTM_Arch(vocab_size=vocab_size)
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
        self.padding_idx = padding_idx
        self.text_transform = text_transform

    def __call__(self, text, prob=True):
        if isinstance(text, str):
            text = [text]
            unpack = True
        else:
            unpack = False
            
        # prepare input     
        input_text = F.to_tensor(self.text_transform(text), padding_value=self.padding_idx)
        
        # predict
        logit = self.model(input_text)
        
        # get probability of each class
        if prob:
            probs = torch.exp(logit)
            if unpack:
                return probs[0,:].tolist()
            else:
                return probs[:,:].tolist()
        else:
            return logit.argmax(1)

def initializeModel():
    print('here')
    # load bert model and tokenizer
    if do_use_bert_large:
        bert = AutoModel.from_pretrained('bert-large-uncased')
        bert_tokenizer = BertTokenizerFast.from_pretrained('bert-large-uncased')    
    else:
        bert = AutoModel.from_pretrained('bert-base-uncased')
        bert_tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
    
    # build a bert based detector
    bert_detector = FakeNewsDetector("BERT", bert, bert_tokenizer, "BERT_based.pt")
    
    # load gpt2 model and tokenizer
    if do_use_gpt2_large:
        gpt2 = AutoModel.from_pretrained('gpt2-medium')
        gpt2_tokenizer = GPT2TokenizerFast.from_pretrained('gpt2-medium')    
    else:
        gpt2 = AutoModel.from_pretrained('gpt2')
        gpt2_tokenizer = GPT2TokenizerFast.from_pretrained('gpt2')
    gpt2_tokenizer.padding_side = "left"
    gpt2_tokenizer.pad_token = gpt2_tokenizer.eos_token
    
    # build a gpt2 based detector
    gpt2_detector = FakeNewsDetector("GPT2", gpt2, gpt2_tokenizer, "GPT2_based.pt")
    
    # LSTM
    padding_idx = 1
    bos_idx = 0
    eos_idx = 2
    max_seq_len = 65
    xlmr_vocab_path = r"https://download.pytorch.org/models/text/xlmr.vocab.pt"
    xlmr_spm_model_path = r"https://download.pytorch.org/models/text/xlmr.sentencepiece.bpe.model"
    
    text_transform = T.Sequential(
        T.SentencePieceTokenizer(xlmr_spm_model_path),
        T.VocabTransform(load_state_dict_from_url(xlmr_vocab_path)),
        T.Truncate(max_seq_len - 2),
        T.AddToken(token=bos_idx, begin=True),
        T.AddToken(token=eos_idx, begin=False),
    )
    vocab = text_transform[1].vocab.vocab
    word_to_idx = vocab.get_stoi()
    
    # build a LSTM detector
    lstm_detector = LSTMDetector(len(vocab), text_transform, padding_idx, "LSTM_based.pt")
    
    # Both bert_detector and gpt2_detector takes text string or a list of text strings as input
    # If input is a text string, output will be a tuple of probabilities, 
    # output[0] is the probability of being truth, output[1] is the probability of being fake
    # If input is a list of text strings, output will be a 2D list with each element being a tuple of probabilities described above
    
    # EXAMPLE:
    text1 = ["If you look at states that are right to work, they constantly do not have budget deficits and they have very good business climates.",
        "Water rates in Manila, Philippines, were raised up to 845 percent when a subsidiary of the World Bank became a partial owner.",
        "Since 2000, nearly 12 million Americans have slipped out of the middle class and into poverty."
    ]
    text2 = "If you look at states that are right to work, they constantly do not have budget deficits and they have very good business climates."
    print(bert_detector(text1))
    print(bert_detector(text2))
    print(gpt2_detector(text1))
    print(gpt2_detector(text2))
    print(lstm_detector(text1))
    print(lstm_detector(text2))
    # END OF EXAMPLE
    
    # TODO
    return bert_detector, gpt2_detector, lstm_detector

if __name__ == "__main__":
    initializeModel()
