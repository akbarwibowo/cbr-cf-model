from flask import Flask, request, jsonify
from cbr_cf import run_prediction

app = Flask(__name__)

@app.route('/', method=['GET'])
def home():
    return "CBR-CF Model"

@app.route('/predict', methods=['POST'])
def main():
    data = request.get_json()
    return jsonify(run_prediction(data))