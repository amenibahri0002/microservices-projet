from flask import Flask, request, jsonify
import statistics

app = Flask(__name__)

@app.route("/mean", methods=['POST'])
def mean():
    data = request.json.get("numbers", [])
    return jsonify({"mean": statistics.mean(data)})

@app.route("/median", methods=['POST'])
def median():
    data = request.json.get("numbers", [])
    return jsonify({"median": statistics.median(data)})

@app.route("/stddev", methods=['POST'])
def stddev():
    data = request.json.get("numbers", [])
    return jsonify({"stddev": statistics.stdev(data)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
