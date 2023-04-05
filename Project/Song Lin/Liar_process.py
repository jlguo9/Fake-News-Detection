import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def load_liar_dataset(train_path, test_path, valid_path):
    col_names = ["id", "label", "statement", "subject", "speaker", "speaker_title", "state", "party",
                 "barely_true_counts", "false_counts", "half_true_counts", "mostly_true_counts", "pants_on_fire_counts",
                 "context"]
    train_data = pd.read_csv(train_path, sep='\t', header=None, names=col_names)
    test_data = pd.read_csv(test_path, sep='\t', header=None, names=col_names)
    valid_data = pd.read_csv(valid_path, sep='\t', header=None, names=col_names)
    
    data = pd.concat([train_data, test_data, valid_data])
    return data

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()
    return text

def data_pipeline(csv_file):
    data = pd.read_csv(csv_file)
    data["statement"] = data["statement"].apply(preprocess_text)

    
    data["text"] = data["statement"]
    data["label"] = data["label"].apply(lambda x: 1 if x == "false" or x == "pants-fire" else 0)

    # Only keep label and text columns
    data = data[["label", "text"]]

    # Save the processed data
    data.to_csv("liar_processed_data.csv", index=False)

    return data

train_path = "./liar_dataset/train.tsv"
test_path = "./liar_dataset/test.tsv"
valid_path = "./liar_dataset/valid.tsv"
data = load_liar_dataset(train_path, test_path, valid_path)

# Save the data to a CSV file
data.to_csv("liar_data.csv", index=False)

# Load data from the CSV file and run the data pipeline
data_pipeline("liar_data.csv")