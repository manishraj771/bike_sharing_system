import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np

# Load the trained model
model = joblib.load('ml_models/demand_model.pkl')

# Example test data (replace with actual test data)
data = pd.DataFrame({
    'location': [1, 2, 3, 4],
    'time_of_day': [12, 18, 22, 6],
    'demand': [100, 150, 50, 200]  # Actual demand (ground truth)
})

# Features and true target values
X_test = data[['location', 'time_of_day']]
y_test = data['demand']

# Make predictions using the trained model
y_pred = model.predict(X_test)

# Calculate evaluation metrics
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R²): {r2}")
