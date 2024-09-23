from flask import Blueprint, request, jsonify
import joblib
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a Flask Blueprint for routes
routes_bp = Blueprint('routes', __name__)

# Load the saved models with error handling
try:
    rf_model_path = os.path.join('ml_models', 'best_RandomForest_model.pkl')
    rf_model = joblib.load(rf_model_path)
    logging.info("RandomForest model loaded successfully.")
except FileNotFoundError:
    logging.error("RandomForest model file not found. Please ensure the model is saved correctly.")
except Exception as e:
    logging.error(f"Error loading RandomForest model: {e}")

try:
    gb_model_path = os.path.join('ml_models', 'best_GradientBoosting_model.pkl')
    gb_model = joblib.load(gb_model_path)
    logging.info("GradientBoosting model loaded successfully.")
except FileNotFoundError:
    logging.error("GradientBoosting model file not found. Please ensure the model is saved correctly.")
except Exception as e:
    logging.error(f"Error loading GradientBoosting model: {e}")

try:
    xgb_model_path = os.path.join('ml_models', 'best_XGBoost_model.pkl')
    xgb_model = joblib.load(xgb_model_path)
    logging.info("XGBoost model loaded successfully.")
except FileNotFoundError:
    logging.error("XGBoost model file not found. Please ensure the model is saved correctly.")
except Exception as e:
    logging.error(f"Error loading XGBoost model: {e}")

# Load the scaler for GradientBoosting and XGBoost models
try:
    scaler_path = os.path.join('ml_models', 'scaler.pkl')
    scaler = joblib.load(scaler_path)
    logging.info("Scaler loaded successfully.")
except FileNotFoundError:
    logging.error("Scaler file not found. Please ensure the scaler is saved correctly.")
except Exception as e:
    logging.error(f"Error loading scaler: {e}")

# Define the feature names used in the model
feature_names = ['location', 'time_of_day', 'weather', 'temperature', 'is_weekend', 'holiday', 'traffic_congestion']

@routes_bp.route('/predict', methods=['POST'])
def predict_demand():
    try:
        # Extract data from the POST request
        data = request.get_json()

        # Validate that all required fields are present
        required_fields = ['location', 'time_of_day', 'weather', 'temperature', 'is_weekend', 'holiday']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Extract features from request
        location = data['location']
        time_of_day = data['time_of_day']
        weather = data['weather']
        temperature = data['temperature']
        is_weekend = data['is_weekend']
        holiday = data['holiday']
        traffic_congestion = data.get('traffic_congestion', 0)  # Optional new feature

        # Create a DataFrame for the new data point with the correct feature names
        new_data = pd.DataFrame({
            'location': [location],
            'time_of_day': [time_of_day],
            'weather': [weather],
            'temperature': [temperature],
            'is_weekend': [is_weekend],
            'holiday': [holiday],
            'traffic_congestion': [traffic_congestion]
        })

        # Ensure the feature names match the model's expected input
        new_data = new_data[feature_names]

        # Select the model dynamically
        model_name = data.get('model', 'RandomForest')  # Default to RandomForest if no model specified
        if model_name == 'GradientBoosting':
                        # Scale the data for GradientBoosting
            new_data_scaled = scaler.transform(new_data)
            prediction = gb_model.predict(new_data_scaled)
        elif model_name == 'XGBoost':
            # Scale the data for XGBoost
            new_data_scaled = scaler.transform(new_data)
            prediction = xgb_model.predict(new_data_scaled)
        else:
            # Use RandomForest by default
            prediction = rf_model.predict(new_data)

        # Return the prediction as a JSON response
        return jsonify({'predicted_demand': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
