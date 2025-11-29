from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Microservice Calculatrice opérationnel 🚀"})

@app.route('/add', methods=['GET'])
def add():
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))
    return jsonify({"result": x + y})

@app.route('/sub', methods=['GET'])
def sub():
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))
    return jsonify({"result": x - y})

@app.route('/mul', methods=['GET'])
def mul():
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))
    return jsonify({"result": x * y})

@app.route('/div', methods=['GET'])
def div():
    x = float(request.args.get('x', 1))
    y = float(request.args.get('y', 1))
    if y == 0:
        return jsonify({"error": "Division par zéro interdite"}), 400
    return jsonify({"result": x / y})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
