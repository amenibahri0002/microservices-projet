from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUESTS = Counter("calculatrice_requests_total", "Total requests to calculator endpoints")

@app.route("/add")
def add():
    REQUESTS.inc()
    x = float(request.args.get("x", 0))
    y = float(request.args.get("y", 0))
    return jsonify({"result": x + y})

@app.route("/sub")
def sub():
    REQUESTS.inc()
    x = float(request.args.get("x", 0))
    y = float(request.args.get("y", 0))
    return jsonify({"result": x - y})

@app.route("/mul")
def mul():
    REQUESTS.inc()
    x = float(request.args.get("x", 0))
    y = float(request.args.get("y", 0))
    return jsonify({"result": x * y})

@app.route("/div")
def div():
    REQUESTS.inc()
    x = float(request.args.get("x", 0))
    y = float(request.args.get("y", 1))
    return jsonify({"result": x / y if y != 0 else None})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
