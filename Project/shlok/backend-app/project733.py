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
    
    # Both bert_detector and gpt2_detector takes text string or a list of text strings as input
    # If input is a text string, output will be a tuple of probabilities, 
    # output[0] is the probability of being truth, output[1] is the probability of being fake
    # If input is a list of text strings, output will be a 2D list with each element being a tuple of probabilities described above
    
    # EXAMPLE:
    text1 = ["Donald Trump Sends Out Embarrassing New Year’s Eve Message; This is Disturbing",
        "WATCH: George W. Bush Calls Out Trump For Supporting White Supremacy",
        "U.S. lawmakers question businessman at 2016 Trump Tower meeting: sources",
        "Trump administration issues new rules on U.S. visa waivers"
    ]
    text2 = "Donald Trump Sends Out Embarrassing New Year’s Eve Message; This is Disturbing"
    print(bert_detector(text1))
    print(bert_detector(text2))
    print(gpt2_detector(text1))
    print(gpt2_detector(text2))
    # END OF EXAMPLE
    
    # TODO
    return bert_detector, gpt2_detector
	
	
def get_results(text):
    r1 = bert_detector(text)
    r2 = gpt2_detector(text)
    return jsonify([{'m':'bert', 'r':r1},{'m':'gpt2', 'r':r2}])


if __name__ == "__main__":
    main()
