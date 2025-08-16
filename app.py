from flask import Flask, request, jsonify
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock training data
data = pd.DataFrame({
    'age': [25, 35, 45, 55, 30],
    'driving_experience_years': [2, 10, 20, 30, 5],
    'vehicle_type': ['car', 'van', 'car', 'motorcycle', 'van'],
    'past_accidents': [1, 0, 0, 1, 2],
    'risk_score': [0.8, 0.2, 0.1, 0.6, 0.7]
})

# Preprocess and train model
try:
    le = LabelEncoder()
    data['vehicle_type'] = le.fit_transform(data['vehicle_type'])
    X = data.drop('risk_score', axis=1)
    y = data['risk_score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = xgb.XGBRegressor()
    model.fit(X_train, y_train)
    logger.info("Model trained successfully")
except Exception as e:
    logger.error(f"Model training failed: {str(e)}")

@app.route('/predict_risk', methods=['POST'])
def predict_risk():
    try:
        logger.info("Predict risk endpoint called")
        input_data = request.json
        logger.debug(f"Input data: {input_data}")
        if not input_data:
            logger.warning("No input data provided")
        required_fields = ['age', 'driving_experience_years', 'vehicle_type', 'past_accidents']
        if not all(field in input_data for field in required_fields):
            logger.warning("Missing required fields")
            return jsonify({'error': 'Missing required fields'}), 400
        if input_data['vehicle_type'] not in ['car', 'van', 'motorcycle']:
            logger.warning(f"Invalid vehicle_type: {input_data['vehicle_type']}")
            return jsonify({'error': 'vehicle_type must be car, van, or motorcycle'}), 400
        df = pd.DataFrame([input_data])
        df['vehicle_type'] = le.transform(df['vehicle_type'])
        prediction = model.predict(df)[0]
        logger.info(f"Prediction: {prediction}")
        return jsonify({'risk_score': float(prediction)})
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    logger.info("Health endpoint called")
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    logger.info("Starting Flask app")
    app.run(host='0.0.0.0', port=5000, debug=True)