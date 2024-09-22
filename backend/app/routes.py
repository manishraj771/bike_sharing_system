from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load('ml_models/demand_model.pkl')

@app.route('/predict', methods=['POST'])
def predict_demand():
    data = request.get_json()

    # Example data format from the POST request
    location = data['location']
    time_of_day = data['time_of_day']
    weather = data['weather']
    temperature = data['temperature']
    is_weekend = data['is_weekend']
    holiday = data['holiday']

    # Make prediction
    prediction = model.predict([[location, time_of_day, weather, temperature, is_weekend, holiday]])

    return jsonify({'predicted_demand': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
