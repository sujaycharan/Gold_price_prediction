from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the saved model
model = joblib.load('gold_price_model.pkl')

@app.route('/')
def home():
    return "Gold Price Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'predicted_gold_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
