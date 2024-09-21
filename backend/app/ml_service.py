import joblib

# Load pre-trained model
model = joblib.load('ml_models/demand_model.pkl')

def predict_demand(location):
    """Predict demand based on location."""
    features = [location]  # Modify as per your feature set
    demand = model.predict([features])[0]
    return demand
