import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load or create a dataset for bike demand prediction (replace with your actual data)
data = pd.DataFrame({
    'location': [1, 2, 3, 4, 1, 2, 3, 4],       
    'time_of_day': [12, 18, 22, 6, 12, 18, 22, 6],  
    'weather': [0, 1, 0, 1, 0, 1, 0, 1],          
    'temperature': [30, 28, 35, 32, 29, 26, 24, 22],  
    'day_of_week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday'],
    'holiday': [0, 0, 0, 1, 0, 0, 0, 1],  # Binary feature: 1 if it's a holiday, else 0
    'demand': [100, 150, 50, 200, 120, 130, 80, 220]
})

# Feature engineering: Add 'is_weekend' feature
data['is_weekend'] = data['day_of_week'].apply(lambda x: 1 if x in ['Saturday', 'Sunday'] else 0)

# Features and Target
X = data[['location', 'time_of_day', 'weather', 'temperature', 'is_weekend', 'holiday']]  # More features
y = data['demand']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'ml_models/demand_model.pkl')

# Evaluate the model
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print(f"Model trained and saved successfully at ml_models/demand_model.pkl")
print(f"RMSE: {rmse}")
print(f"R²: {r2}")
