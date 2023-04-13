import re
import pandas as pd
import tweepy
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read("config.ini")

# Get the API keys and tokens from the configuration file
API_KEY = config["twitter"]["API_KEY"]
API_SECRET_KEY = config["twitter"]["API_SECRET_KEY"]
ACCESS_TOKEN = config["twitter"]["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = config["twitter"]["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuth1UserHandler(
    API_KEY,
    API_SECRET_KEY,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

accounts = ['CNN', 'BBC', 'ABC', 'AP']

tweets = []
for account in accounts:
    results = api.user_timeline(screen_name=account, tweet_mode="extended", count=100)
    tweets.extend(results)

def remove_emoji(string):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r'', string)

def extract_hashtags(text):
    hashtags = re.findall(r"#(\w+)", text)
    return hashtags

def extract_links(text):
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return links

def preprocess_text(text):
    text = text.lower()
    # Extract hashtags
    hashtags = extract_hashtags(text)
    # Remove links
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    # Remove special symbols and punctuation
    text = re.sub(r"[^a-zA-Z0-9\s#]", "", text)
    # Remove multiple consecutive spaces
    text = re.sub(r'\s{2,}', ' ', text)
    return text, hashtags

texts = []
hashtags_list = []
tweet_ids = []
usernames = []
links = []
for tweet in tweets:
    try:
        text = tweet.retweeted_status.full_text
    except AttributeError:
        text = tweet.full_text
    preprocessed_text, hashtags = preprocess_text(text)
    extracted_links = extract_links(text)
    texts.append(preprocessed_text)
    hashtags_list.append(hashtags)
    tweet_ids.append(tweet.id)
    usernames.append(tweet.user.screen_name)
    links.append(extracted_links)

data = pd.DataFrame({"tweet_id": tweet_ids, "username": usernames, "text": texts, "hashtags": hashtags_list, "links": links})
data.to_csv("news_data.csv", index=False)
