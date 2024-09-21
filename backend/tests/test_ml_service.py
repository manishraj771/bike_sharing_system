import joblib
import pandas as pd

def test_load_model():
    """Test if the demand model is loaded correctly."""
    model = joblib.load('ml_models/demand_model.pkl')
    assert model is not None, "Model could not be loaded"

def test_model_prediction():
    """Test the prediction of the loaded model."""
    model = joblib.load('ml_models/demand_model.pkl')

    # Test data
    data = pd.DataFrame({
        'location': [1, 2],
        'time_of_day': [12, 18]
    })

    # Make predictions
    predictions = model.predict(data)

    assert len(predictions) == 2, "Model did not return correct number of predictions"
