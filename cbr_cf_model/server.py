from flask import Flask, request, jsonify
from cbr_cf import run_prediction

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def main():
    data = request.get_json()
    return jsonify(run_prediction(data))


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
