import joblib
import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Example dataset (replace with real data)
data = pd.DataFrame({
    'location': [1, 2, 3, 4, 1, 2, 3, 4],
    'time_of_day': [12, 18, 22, 6, 12, 18, 22, 6],
    'weather': [0, 1, 0, 1, 0, 1, 0, 1],  # 0 for clear, 1 for rainy (example)
    'temperature': [30, 28, 35, 32, 29, 26, 24, 22],
    'day_of_week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday'],
    'holiday': [0, 0, 0, 1, 0, 0, 0, 1],  # 1 for holiday, 0 for regular day
    'demand': [100, 150, 50, 200, 120, 130, 80, 220]  # Target variable (demand for bikes)
})

# Feature engineering: Add is_weekend feature
data['is_weekend'] = data['day_of_week'].apply(lambda x: 1 if x in ['Saturday', 'Sunday'] else 0)

# Features and Target
X = data[['location', 'time_of_day', 'weather', 'temperature', 'is_weekend', 'holiday']]
y = data['demand']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter grid for RandomForest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

# Perform GridSearchCV to find the best hyperparameters
grid_search = GridSearchCV(RandomForestRegressor(), param_grid, cv=3, scoring='neg_root_mean_squared_error')
grid_search.fit(X_train, y_train)

# Retrieve the best model from GridSearch
best_model = grid_search.best_estimator_
print(f"Best Parameters: {grid_search.best_params_}")

# Save the best model
joblib.dump(best_model, 'ml_models/best_random_forest_model.pkl')

# Make predictions on the test data
y_pred = best_model.predict(X_test)

# Calculate evaluation metrics
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print(f"Best Model RMSE: {rmse}")
print(f"Best Model R²: {r2}")

# Cross-Validation: Ensure the model generalizes well
cv_scores = cross_val_score(best_model, X, y, cv=5, scoring='neg_root_mean_squared_error')
print(f"Cross-Validation RMSE: {-cv_scores.mean()}")

# Feature Importance: Understand the importance of each feature
feature_importances = best_model.feature_importances_
plt.bar(X.columns, feature_importances)
plt.title('Feature Importance')
plt.show()

# Predict demand for a new data point (useful when integrating into an API)
new_data = pd.DataFrame({
    'location': [3],
    'time_of_day': [14],
    'weather': [1],  # Rainy weather
    'temperature': [28],
    'is_weekend': [0],
    'holiday': [0]
})

new_prediction = best_model.predict(new_data)
print(f"Predicted demand for the new data: {new_prediction[0]}")
