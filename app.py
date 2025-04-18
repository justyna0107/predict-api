from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    # Pobierz liczby z parametrów URL, domyślnie 0 jeśli brak
    try:
        x = float(request.args.get('x', 0))
    except ValueError:
        x = 0

    try:
        y = float(request.args.get('y', 0))
    except ValueError:
        y = 0

    suma = x + y
    prediction = 1 if suma > 5.8 else 0

    response = {
        "features": {"x": x, "y": y},
        "prediction": prediction
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
