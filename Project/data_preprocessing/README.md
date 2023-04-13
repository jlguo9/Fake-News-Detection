# Data Preprocessing Repository

This repository contains the necessary scripts and notebooks for preprocessing and exploring various fake news datasets, including Liar, BuzzFeed, and PHEME datasets.

	Directory Structure
	.
	├── Buzz_process.py
	├── EDALiar.ipynb
	├── EDA_buzzfeed.ipynb
	├── Liar_process.py
	├── PHEME
	│   ├── EDA
	│   │   ├── EDA.ipynb
	│   │   └── pheme_to_csv.ipynb
	│   ├── PHEME.zip
	│   └── README.md
	├── PHEME_process.py
	├── buzzfeed
	│   ├── BuzzFeedNews.txt
	│   ├── BuzzFeedNewsUser.txt
	│   ├── BuzzFeedUser.txt
	│   ├── BuzzFeedUserFeature.mat
	│   ├── BuzzFeedUserUser.txt
	│   ├── BuzzFeed_fake_news_content.csv
	│   ├── BuzzFeed_real_news_content.csv
	│   ├── PolitiFactNews.txt
	│   ├── PolitiFactNewsUser.txt
	│   ├── PolitiFactUser.txt
	│   ├── PolitiFactUserFeature.mat
	│   ├── PolitiFactUserUser.txt
	│   ├── PolitiFact_fake_news_content.csv
	│   └── PolitiFact_real_news_content.csv
	├── buzzfeed_data.zip
	├── data_integration
	│   ├── cleaned_dataset.zip
	│   ├── data.csv
	│   └── data_integration.ipynb
	└── liar
	    ├── README
	    ├── test.tsv
	    ├── train.tsv
	    └── valid.tsv
### Files and Directories

Buzz_process.py: Script to process BuzzFeed dataset.
EDALiar.ipynb: Exploratory Data Analysis (EDA) notebook for Liar dataset.
EDA_buzzfeed.ipynb: EDA notebook for BuzzFeed dataset.
Liar_process.py: Script to process Liar dataset.
PHEME_process.py: Script to process PHEME dataset.
### PHEME
PHEME/EDA/EDA.ipynb: EDA notebook for PHEME dataset.
PHEME/EDA/pheme_to_csv.ipynb: Script to convert PHEME dataset to CSV format.
PHEME/PHEME.zip: Zipped PHEME dataset.
PHEME/README.md: Readme file for PHEME dataset.
### buzzfeed
buzzfeed/: Directory containing BuzzFeed dataset files.
buzzfeed_data.zip: Zipped BuzzFeed dataset.
### data_integration
data_integration/cleaned_dataset.zip: Zipped cleaned dataset after integration.
data_integration/data.csv: Integrated dataset in CSV format.
data_integration/data_integration.ipynb: merges several cleaned dataset together to form a data.csv file which can be used by the models. It takes buzzfeed_data.csv, liar_data.csv, pheme_data.csv, Kaggle_Fake.csv, Kaggle_True.csv as input and gives data.csv as output. To run it, put it under the same folder of the above csv files first (examples can be find in cleaned_dataset.zip), and click run all.



### liar
liar/: Directory containing Liar dataset files.