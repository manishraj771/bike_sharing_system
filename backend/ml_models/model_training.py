import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Example dataset with all the necessary features
data = pd.DataFrame({
    'location': [1, 2, 3, 4, 1, 2, 3, 4],
    'time_of_day': [12, 18, 22, 6, 12, 18, 22, 6],
    'weather': [0, 1, 0, 1, 0, 1, 0, 1],  # 0 for clear, 1 for rainy
    'temperature': [30, 28, 35, 32, 29, 26, 24, 22],  # Temperature in Celsius
    'is_weekend': [0, 0, 0, 0, 1, 1, 1, 1],  # 1 for weekend, 0 for weekday
    'holiday': [0, 1, 0, 1, 0, 0, 1, 1],  # 1 for holiday, 0 for non-holiday
    'demand': [100, 150, 50, 200, 120, 130, 80, 220]  # Target variable (demand for bikes)
})

# Features and Target
X = data[['location', 'time_of_day', 'weather', 'temperature', 'is_weekend', 'holiday']]
y = data['demand']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model with RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model to the `ml_models` directory
model_path = 'ml_models/demand_model.pkl'
joblib.dump(model, model_path)

print(f"Model trained and saved successfully to {model_path}.")

# Evaluate the model on the test data
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print(f"Model Evaluation on Test Data:")
print(f"RMSE: {rmse}")
print(f"R²: {r2}")
