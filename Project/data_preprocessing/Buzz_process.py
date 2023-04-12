import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def load_buzzfeed_dataset(buzzfeed_real_path, buzzfeed_fake_path):
    buzzfeed_real = pd.read_csv(buzzfeed_real_path)
    buzzfeed_fake = pd.read_csv(buzzfeed_fake_path)
    buzzfeed_df = pd.concat([buzzfeed_real, buzzfeed_fake])
    del buzzfeed_real, buzzfeed_fake

    buzzfeed_df["type"] = buzzfeed_df["id"].apply(lambda x: x.split("_")[0])
    buzzfeed_df = buzzfeed_df[["id", "title", "text", "source", "type", "images", "movies"]]
    buzzfeed_df["movies"] = buzzfeed_df["movies"].apply(lambda x: 1 if not pd.isna(x) else 0)
    buzzfeed_df["images"] = buzzfeed_df["images"].apply(lambda x: 1 if not pd.isna(x) else 0)

    return buzzfeed_df

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()
    return text

def data_pipeline(csv_file):
    data = pd.read_csv(csv_file)
    #print(data['type'])
    #input()
    data["text"] = data["text"].apply(preprocess_text)

    data["label"] = data["type"].apply(lambda x: 1 if x == "Fake" else 0)

    
    # Only keep label and text columns
    data = data[["label", "text"]]

    # Save the processed data
    data.to_csv("buzz_processed_data.csv", index=False)

    return data

buzzfeed_real_path = "./buzzfeed/BuzzFeed_real_news_content.csv"
buzzfeed_fake_path = "./buzzfeed/BuzzFeed_fake_news_content.csv"
data = load_buzzfeed_dataset(buzzfeed_real_path, buzzfeed_fake_path)

# Save the data to a CSV file
data.to_csv("buzzfeed_data.csv", index=False)

# Load data from the CSV file and run the data pipeline
data_pipeline("buzzfeed_data.csv")


