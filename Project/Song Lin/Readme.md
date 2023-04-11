## Readme

This repository contains code and resources for the Fake News Detection project, which aims to build a fake news detection data product using BERT, GPT-2, and LSTM models. The project also includes the evaluation and comparison of these models' performances across different news categories and time periods.

	.
	├── dataAnalyze
	│   ├── IFND.csv
	│   ├── analyze_report.pdf
	│   ├── datawithdate.ipynb
	│   ├── pre
	│   │   ├── INFD_Pred.csv
	│   │   ├── bert_pred.csv
	│   │   ├── gpt2_pred.csv
	│   │   └── lstm_pred.csv
	│   └── shap_lime_analyze.ipynb
	├── dataPreprocess
	│   ├── Buzz_process.py
	│   ├── EDAofliar.ipynb
	│   ├── Liar_process.py
	│   ├── PHEME_process.py
	│   └── liar_dataset
	│       ├── README
	│       ├── test.tsv
	│       ├── train.tsv
	│       └── valid.tsv
	├── liveData
	│   ├── auto_label_openai.py
	│   ├── config.ini
	│   ├── get_twitter_data.ipynb
	│   └── openai_test.ipynb
	└── pics
	    ├── 2018.png
	    ├── WeChat7387df3ff5214e93ecc5a8b08cf9ee17.png
	    ├── graph.png
	    ├── lime_explanation.html
	    ├── project-5.drawio
	    ├── project.drawio-4.png
	    └── shap.png
## Description of Directories and Files

dataAnalyze: Contains the main dataset (IFND.csv), analysis report (analyze_report.pdf), data analysis notebooks (datawithdate.ipynb and shap_lime_analyze.ipynb), and model predictions (pre folder).
dataPreprocess: Contains the preprocessing scripts for different datasets (Buzz_process.py, Liar_process.py, PHEME_process.py), an exploratory data analysis notebook (EDAofliar.ipynb), and the Liar dataset (liar_dataset folder).
liveData: Contains scripts for collecting and labeling live data from Twitter using OpenAI models (auto_label_openai.py, get_twitter_data.ipynb, openai_test.ipynb), and a configuration file (config.ini).
pics: Contains images and visualizations used in the project, including LIME and SHAP explanations (lime_explanation.html, shap.png), project diagrams (project-5.drawio, project.drawio-4.png), and other visualizations (2018.png, WeChat7387df3ff5214e93ecc5a8b08cf9ee17.png, graph.png).

## Usage

Clone the repository to your local machine.
Install required packages from the requirements.txt file.
Run the preprocessing scripts to process the datasets.
Train and evaluate the models using the provided Jupyter notebooks.
Analyze the results using LIME and SHAP techniques in the shap_lime_analyze.ipynb notebook.
Collect and label live data from Twitter using the get_twitter_data.ipynb and auto_label_openai.py scripts.