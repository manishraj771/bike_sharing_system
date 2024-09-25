from flask import Blueprint, request, jsonify
import joblib
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging
from app.services.payment_service import process_payment
from app.services.alert_service import send_notification
from app.dynamic_pricing import calculate_price  # Corrected import path

# Define a Flask Blueprint for routes
routes_bp = Blueprint('routes', __name__)

# Load models with error handling
try:
    rf_model_path = os.path.join('ml_models', 'best_RandomForest_model.pkl')
    rf_model = joblib.load(rf_model_path)
    logging.info("RandomForest model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading RandomForest model: {e}")

try:
    gb_model_path = os.path.join('ml_models', 'best_GradientBoosting_model.pkl')
    gb_model = joblib.load(gb_model_path)
    logging.info("GradientBoosting model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading GradientBoosting model: {e}")

try:
    xgb_model_path = os.path.join('ml_models', 'best_XGBoost_model.pkl')
    xgb_model = joblib.load(xgb_model_path)
    logging.info("XGBoost model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading XGBoost model: {e}")

# Load the scaler for GradientBoosting and XGBoost models
try:
    scaler_path = os.path.join('ml_models', 'scaler.pkl')
    scaler = joblib.load(scaler_path)
    logging.info("Scaler loaded successfully.")
except Exception as e:
    logging.error(f"Error loading scaler: {e}")

# Define the feature names used in the model (without 'traffic_congestion')
feature_names = ['location', 'time_of_day', 'weather', 'temperature', 'is_weekend', 'holiday']

@routes_bp.route('/predict', methods=['POST'])
def predict_demand():
    """Predict bike demand and calculate dynamic pricing."""
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
            'holiday': [holiday]
        })

        # Ensure the feature names match the model's expected input
        new_data = new_data[feature_names]

        # Select the model dynamically
        model_name = data.get('model', 'RandomForest')  # Default to RandomForest if no model specified
        if model_name == 'GradientBoosting':
            new_data_scaled = scaler.transform(new_data)  # Scale the data for GradientBoosting
            prediction = gb_model.predict(new_data_scaled)
        elif model_name == 'XGBoost':
            new_data_scaled = scaler.transform(new_data)  # Scale the data for XGBoost
            prediction = xgb_model.predict(new_data_scaled)
        else:
            prediction = rf_model.predict(new_data)  # Use RandomForest by default

        # Convert prediction to Python native type before returning it
        prediction_value = float(prediction[0])

        # Calculate dynamic pricing based on predicted demand
        price = calculate_price(prediction_value)

        # Return the prediction and dynamic pricing as a JSON response
        return jsonify({'predicted_demand': prediction_value, 'dynamic_price': price})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@routes_bp.route('/book', methods=['POST'])
def book_bike():
    """Book a bike and process payment."""
    try:
        # Get the payment details from the request
        data = request.get_json()
        user_id = data.get('user_id')
        amount = data.get('amount')

        if not user_id or amount is None:
            return jsonify({"status": "failed", "message": "Invalid request, missing user_id or amount."}), 400

        # Call the payment service to process the payment
        payment_result = process_payment(user_id, amount)

        # Handle payment failure
        if payment_result['status'] == 'failed':
            send_notification(user_id, "Payment failed for booking.")
            return jsonify(payment_result), 400

        # Simulate bike booking logic after successful payment
        send_notification(user_id, "Your bike has been booked successfully.")
        return jsonify({"status": "success", "message": "Bike booked successfully.", "payment_details": payment_result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
