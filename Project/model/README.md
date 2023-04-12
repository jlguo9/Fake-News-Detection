## Models

All the three models take data.csv as input, which is a dataset after cleaning and integration. An example can be find at /Project/data_preprocessing/data_integration/data.csv

### BERT_based.ipynb

Put the Jupyter notebook under the same folder with dataset and run all. The notebook saves trained model as BERT_based.pt, logs the training and validation performance, and gives a classification report and a confusion matrix on test set.

### GPT2_based.ipynb

Put the Jupyter notebook under the same folder with dataset and run all. The notebook saves trained model as GPT2_based.pt, logs the training and validation performance, and gives a classification report and a confusion matrix on test set.

### LSTM_based.ipynb

Put the Jupyter notebook under the same folder with dataset and run all. The notebook saves trained model as LSTM_based.pt, logs the training and validation performance, and gives a classification report and a confusion matrix on test set.

## Detectors

detector.py contains the detector class of the three models. Put the script under the same folder with BERT_based.pt, GPT2_based.pt, and LSTM_based.pt, and run it by

    $ Python detector.py

the detector.py will return three detectors which can take text as input and give probabilities of two classes as output. An example is included in the script. This script is used in the web app connected to the backend server later.