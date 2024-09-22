import sys
import os
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Add the directory to sys.path to make sure the app can be found
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Initialize the Flask app
from app import create_app
app = create_app()

# Load the best model (RandomForest model trained earlier)
model = joblib.load('ml_models/best_random_forest_model.pkl')

# Define the predict route to handle POST requests
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features from request data
    location = data['location']
    time_of_day = data['time_of_day']
    weather = data['weather']
    temperature = data['temperature']
    is_weekend = data['is_weekend']
    holiday = data['holiday']

    # Create a DataFrame for the new data point
    new_data = pd.DataFrame({
        'location': [location],
        'time_of_day': [time_of_day],
        'weather': [weather],
        'temperature': [temperature],
        'is_weekend': [is_weekend],
        'holiday': [holiday]
    })

    # Make the prediction using the loaded model
    prediction = model.predict(new_data)

    return jsonify({'predicted_demand': prediction[0]})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
