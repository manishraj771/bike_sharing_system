import pandas as pd

# Load the original datasets from the 'data/' directory
day_data = pd.read_csv('ml_models/data/day.csv')  
hour_data = pd.read_csv('ml_models/data/hour.csv')

# Display basic info about the original datasets
print("Daily Data Info:")
print(day_data.info())
print("\nHourly Data Info:")
print(hour_data.info())

# External weather data: You would replace this with real external data in production
external_weather_data = pd.DataFrame({
    'dteday': ['2011-01-01', '2011-01-02', '2011-01-03'],  # Sample dates (should match the format in 'day.csv')
    'precipitation': [0.2, 0.0, 0.1],   # Sample precipitation data (real data should be fetched from an API)
    'visibility': [10, 12, 8]           # Sample visibility data (replace with actual weather data)
})

# Merge external weather data with the day_data DataFrame on the date field ('dteday')
day_data = pd.merge(day_data, external_weather_data, on='dteday', how='left')

# Feature Engineering: Add rolling temperature averages to capture trends
day_data['rolling_temp'] = day_data['temp'].rolling(window=3).mean()

# Add additional features (e.g., interaction terms, lag features)
# Example: Lag the 'cnt' column by 1 day to capture rental counts from the previous day
day_data['previous_day_cnt'] = day_data['cnt'].shift(1)

# Check for missing values after the merge (e.g., if some days have no weather data)
print("\nMissing values after merging external weather data:")
print(day_data.isnull().sum())

# Save the enhanced dataset to a new CSV file in the 'ml_models/data/' directory
augmented_file_path = 'ml_models/data/day_augmented.csv'
day_data.to_csv(augmented_file_path, index=False)
print(f"\nEnhanced dataset saved to {augmented_file_path}")
