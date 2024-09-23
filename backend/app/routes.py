from flask import Blueprint, request, jsonify
import joblib
import os
import pandas as pd

# Define a Flask Blueprint for routes
routes_bp = Blueprint('routes', __name__)

# Load the saved model
model_path = os.path.join('ml_models', 'demand_model.pkl')
model = joblib.load(model_path)

# Define the feature names used in the model
feature_names = ['location', 'time_of_day', 'weather', 'temperature', 'is_weekend', 'holiday']

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

        # Create a DataFrame for the new data point with the correct feature names
        new_data = pd.DataFrame({
            'location': [data['location']],
            'time_of_day': [data['time_of_day']],
            'weather': [data['weather']],
            'temperature': [data['temperature']],
            'is_weekend': [data['is_weekend']],
            'holiday': [data['holiday']]
        })

        # Ensure the feature names match the model's expected input
        new_data = new_data[feature_names]

        # Make prediction using the model
        prediction = model.predict(new_data)

        # Return the prediction as a JSON response
        return jsonify({'predicted_demand': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
