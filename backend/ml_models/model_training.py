import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Example data for training (replace this with actual data from your CSV or database)
data = pd.DataFrame({
    'location': [1, 2, 3, 4],          # Location of the bike station (categorical)
    'time_of_day': [12, 18, 22, 6],    # Time of the day (hours)
    'demand': [100, 150, 50, 200]      # Demand for bikes (target variable)
})

# Splitting the data into features (X) and target (y)
X = data[['location', 'time_of_day']]  # Features (independent variables)
y = data['demand']  # Target variable

# Splitting the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a Random Forest Regressor
model = RandomForestRegressor()

# Train the model
model.fit(X_train, y_train)

# Save the trained model to the ml_models directory
joblib.dump(model, 'ml_models/demand_model.pkl')

print("Model trained and saved successfully.")
