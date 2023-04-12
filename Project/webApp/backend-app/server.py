from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from project733 import *

app = Flask(__name__)
m1 = None
m2= None
CORS(app)


def run_model(newsObj):
    r1 = m1(newsObj['description'])
    r2 = m2(newsObj['description'])
    r3 = m3(newsObj['description'])
    return jsonify([
        {
        "modelId": 1,
        "model":"Bert",
        "fake": r1[1]
        },
        {
        "modelId": 2,
        "model":"GPT2",
        "fake": r2[1]
        },
        {
        "modelId": 3,
        "model":"LSTM",
        "fake": r3[1]
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
    
