import joblib
import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

# Example dataset (replace with real data)
data = pd.DataFrame({
    'location': [1, 2, 3, 4, 1, 2, 3, 4],
    'time_of_day': [12, 18, 22, 6, 12, 18, 22, 6],
    'weather': [0, 1, 0, 1, 0, 1, 0, 1],
    'temperature': [30, 28, 35, 32, 29, 26, 24, 22],
    'day_of_week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday'],
    'holiday': [0, 0, 0, 1, 0, 0, 0, 1],
    'demand': [100, 150, 50, 200, 120, 130, 80, 220]
})

# Feature engineering
data['is_weekend'] = data['day_of_week'].apply(lambda x: 1 if x in ['Saturday', 'Sunday'] else 0)

# Features and Target
X = data[['location', 'time_of_day', 'weather', 'temperature', 'is_weekend', 'holiday']]
y = data['demand']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Data scaling (important for Gradient Boosting and XGBoost)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the scaler
joblib.dump(scaler, 'ml_models/scaler.pkl')

# RandomForest parameter grid
rf_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

# GradientBoosting parameter grid
gb_param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7]
}

# XGBoost parameter grid
xgb_param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7]
}

# Train RandomForest
rf_model = RandomForestRegressor()
rf_grid_search = GridSearchCV(rf_model, rf_param_grid, cv=3, scoring='neg_root_mean_squared_error')
rf_grid_search.fit(X_train, y_train)
best_rf_model = rf_grid_search.best_estimator_

# Train GradientBoosting
gb_model = GradientBoostingRegressor()
gb_grid_search = GridSearchCV(gb_model, gb_param_grid, cv=3, scoring='neg_root_mean_squared_error')
gb_grid_search.fit(X_train_scaled, y_train)
best_gb_model = gb_grid_search.best_estimator_

# Train XGBoost
xgb_model = XGBRegressor()
xgb_grid_search = GridSearchCV(xgb_model, xgb_param_grid, cv=3, scoring='neg_root_mean_squared_error')
xgb_grid_search.fit(X_train_scaled, y_train)
best_xgb_model = xgb_grid_search.best_estimator_

# Save the best models
joblib.dump(best_rf_model, 'ml_models/best_RandomForest_model.pkl')
joblib.dump(best_gb_model, 'ml_models/best_GradientBoosting_model.pkl')
joblib.dump(best_xgb_model, 'ml_models/best_XGBoost_model.pkl')

print("Models trained and saved successfully.")
