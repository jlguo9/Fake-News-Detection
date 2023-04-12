import os
import json
import re
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

nltk.download("stopwords")


def load_pheme_dataset(path_to_pheme):
    data = []

    for event in os.listdir(path_to_pheme):
        event_path = os.path.join(path_to_pheme, event)

        if os.path.isdir(event_path):
            for rumor_type in ["rumours", "non-rumours"]:
                rumor_path = os.path.join(event_path, rumor_type)
                for tweet_id in os.listdir(rumor_path):
                    tweet_file = os.path.join(rumor_path, tweet_id, "source-tweets", f"{tweet_id}.json")

                    if os.path.isfile(tweet_file):
                        with open(tweet_file, "r") as file:
                            tweet_data = json.load(file)
                            text = tweet_data["text"]
                            label = 1 if rumor_type == "rumours" else 0
                            user_mentions = " ".join([mention["screen_name"] for mention in tweet_data["entities"]["user_mentions"]])
                            data.append({"id": tweet_id, "label": label, "text": text, "user_mentions": user_mentions})

    return pd.DataFrame(data)


def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Keep only alphabetical characters and whitespace
    text = text.lower()  # Convert to lowercase
    return text


def data_pipeline(csv_file):
    data = pd.read_csv(csv_file)
    data["text"] = data["text"].apply(preprocess_text)

    # Only keep label and text columns
    data = data[["label", "text"]]

    # Save the processed data
    data.to_csv("pheme_processed_data.csv", index=False)

    return data


path_to_pheme = "./PHEME/all-rnr-annotated-threads"
data = load_pheme_dataset(path_to_pheme)

# Save the data to a CSV file
data.to_csv("pheme_data.csv", index=False)

# Load data from the CSV file and run the data pipeline
data_pipeline("pheme_data.csv")