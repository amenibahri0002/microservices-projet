from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Microservice Statistiques opérationnel 🚀"})

@app.route('/mean', methods=['GET'])
def mean():
    numbers = request.args.get('numbers', '')
    try:
        nums = [float(n) for n in numbers.split(',') if n]
        if not nums:
            return jsonify({"error": "Aucune donnée fournie"}), 400
        return jsonify({"mean": sum(nums)/len(nums)})
    except ValueError:
        return jsonify({"error": "Valeurs numériques invalides"}), 400

if __name__ == "__main__":
    # Important : host="0.0.0.0" pour que Kubernetes puisse accéder au container
    # Le port doit correspondre au containerPort dans le YAML (8080)
    app.run(host="0.0.0.0", port=8080)
