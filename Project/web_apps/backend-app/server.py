from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from project733 import *

app = Flask(__name__)
m1 = None
m2 = None
m3 = None
CORS(app)


credibility= {
    'nytimes.com': 0.02,
    'washingtonpost.com': 0.02,
    'wsj.com': 0.02,
    'apnews.com': 0.02,
    'bloomberg.com': 0.02,
    'bcc.com': 0.02,
    'theguardian.com': 0.02,
    'reuters.com': 0.02,
    'cctv.com': -0.05,
    'xinhuanet.com': -0.05,
    'dailymail.co.uk': -0.02,
    'huffpost.com': -0.02,
    'forbes.com': -0.05,
    'gizmodo.com': -0.02,
    'qsheory.com': -0.05,
    'infowars.com': -0.1,
    'dailystar.co.uk': -0.1,
    'nationalenquirer.com': -0.1,
    'breitbart.com': -0.1,
    'beforeitsnews.com': -0.1,
    'globalresearch.ca': -0.1,
    'yournewswire.com': -0.1,
    'worldtruth.tv': -0.1,
    'zerohedge.com': -0.1,
}

def run_model(newsObj):
    source = newsObj['source']
    r1 = m1(newsObj['description'])[1]
    r2 = m2(newsObj['description'])[1]
    r3 = m3(newsObj['description'])[1]
    if source in credibility:
        r1 -= credibility[source]
        r2 -= credibility[source]
        r3 -= credibility[source]
    return jsonify([
        {
        "modelId": 1,
        "model":"Bert",
        "fake": r1
        },
        {
        "modelId": 2,
        "model":"GPT2",
        "fake": r2
        },
        {
        "modelId": 3,
        "model":"LSTM",
        "fake": r3
        }
    ])
    


def feedback_to_model(newsObj):
    # print(newsObj['feedback_value'])
    with open('log', 'a+') as f:
        f.write(json.dumps(newsObj))

@app.route("/")
def home():
    return "Hello, World!"


@app.route('/evaluate-model', methods=['GET', 'POST'])
def evaluate_model():
    # if request.method == 'POST':
    return run_model(request.get_json(force=True))
    
    

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_to_model(request.get_json(force=True))
    return '',201

if __name__ == '__main__':
	m1, m2, m3 = initializeModel()
	app.run(host='0.0.0.0', port=9090)
    
