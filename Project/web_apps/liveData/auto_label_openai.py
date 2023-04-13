import openai
import pandas as pd

openai.api_key = "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"

def check_truthfulness(prompt):
    stop = ["and", "but", "however", "despite"]
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt + "Just give me true or false",
        max_tokens=256,
        n=1,
        stop=stop,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Load data from fake_news_data.csv
data = pd.read_csv("news_data.csv")

labeled_data = []
for index, row in data.iterrows():
    text = row['text']
    result = check_truthfulness(text)
    if "true" in result.lower():
        label = 0
    else:
        label = 1
    labeled_data.append((row['tweet_id'], row['username'], text, row['links'], label))

labeled_df = pd.DataFrame(labeled_data, columns=["tweet_id", "username", "text", "links", "label"])
print(labeled_df)
labeled_df.to_csv("labeled_fake_news_data.csv", index=False)
