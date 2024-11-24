import pickle
from flask import Flask, request, jsonify

# Load the trained model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the House Price Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()
        features = data.get('features')  # Expecting a list of 8 numbers
        if not features or len(features) != 8:
            return jsonify({"error": "Please provide a valid feature array of length 8"}), 400

        # Make prediction
        prediction = model.predict([features])[0]
        
        return jsonify({
            "features": features,
            "predicted_price": round(prediction, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
