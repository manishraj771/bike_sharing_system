import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Example data for training (you should replace this with actual data)
# Assume you have a DataFrame with features `location`, `time_of_day`, etc.
data = pd.DataFrame({
    'location': [1, 2, 3, 4],
    'time_of_day': [12, 18, 22, 6],
    'demand': [100, 150, 50, 200]
})

# Features and labels
X = data[['location', 'time_of_day']]  # Features
y = data['demand']  # Target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestRegressor (or any other model)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model to the `ml_models` directory
joblib.dump(model, 'ml_models/demand_model.pkl')

print("Model trained and saved successfully.")
