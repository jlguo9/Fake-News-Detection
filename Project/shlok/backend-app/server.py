from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def run_model(newsObj):
    print(newsObj['title'])


def feedback_to_model(newsObj):
    print(newsObj['feedback_value'])

@app.route("/")
def home():
    return "Hello, World!"


@app.route('/evaluate-model', methods=['GET', 'POST'])
def evaluate_model():
    # if request.method == 'POST':
    run_model(request.get_json(force=True))
    return jsonify([
        {
        "modelId": 1,
        "model":"Model 1",
        "fake": 6
        },
        {
        "modelId": 2,
        "model":"Model 2",
        "fake": 70
        },
        {
        "modelId": 3,
        "model":"Model 3",
        "fake": 66
        },
        {
        "modelId": 4,
        "model":"Model 4",
        "fake": 55
        }
    ])
    

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_to_model(request.get_json(force=True))
    return '',201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)