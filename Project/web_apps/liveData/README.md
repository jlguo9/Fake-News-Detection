# Live data

A brief description of the project: This project aims to simulate the process of real-time updating of mainstream media news, followed by manual labeling for validation. The goal is to verify our idea of adding real-time data and generating labels for training models in a dynamic manner.

## Directory Structure

	.
	├── auto_label_openai.py          # Script to auto-label news data using OpenAI's GPT-3
	├── config.ini                    # Configuration file for API keys and other settings
	├── get_live_data.py              # Script to fetch live news data from Twitter
	└── news_data.csv                 # Collected news data in CSV format

## Usage

1. Configure the `config.ini` file with your Twitter API credentials.
2. Run `get_live_data.py` to fetch live news data from Twitter and save it to `news_data.csv`.
3. Set your OpenAI API key in `auto_label_openai.py` and run the script to auto-label the news data using OpenAI's GPT-3.
4. The labeled news data will be saved to `labeled_fake_news_data.csv`.