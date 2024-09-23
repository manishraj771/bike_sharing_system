import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Update file paths
day_data = pd.read_csv('data/day.csv')  # Correct path for day.csv
hour_data = pd.read_csv('data/hour.csv')  # Correct path for hour.csv

# Rest of the visualization code...
sns.set(style="whitegrid")

# Visualization 1: Bike rentals over time (daily)
plt.figure(figsize=(10, 6))
plt.plot(day_data['dteday'], day_data['cnt'], label='Total Rentals', color='blue')
plt.title('Bike Rentals Over Time (Daily)')
plt.xlabel('Date')
plt.ylabel('Number of Rentals')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 2: Bike rentals by season
plt.figure(figsize=(8, 6))
sns.boxplot(x='season', y='cnt', data=day_data)
plt.title('Bike Rentals by Season')
plt.xlabel('Season (1: Spring, 2: Summer, 3: Fall, 4: Winter)')
plt.ylabel('Number of Rentals')
plt.show()

# Visualization 3: Temperature vs. Bike rentals
plt.figure(figsize=(8, 6))
plt.scatter(day_data['temp'], day_data['cnt'], color='green', alpha=0.6)
plt.title('Bike Rentals vs. Temperature')
plt.xlabel('Normalized Temperature')
plt.ylabel('Number of Rentals')
plt.show()

# Visualization 4: Hourly rentals by working day
plt.figure(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', hue='workingday', data=hour_data, palette='coolwarm')
plt.title('Hourly Bike Rentals (Working Day vs. Non-Working Day)')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Rentals')
plt.legend(title='Working Day', loc='upper right')
plt.show()

# Visualization 5: Bike rentals by weather condition
plt.figure(figsize=(8, 6))
sns.boxplot(x='weathersit', y='cnt', data=hour_data)
plt.title('Bike Rentals by Weather Condition')
plt.xlabel('Weather Situation (1: Clear, 2: Mist, 3: Light Rain/Snow)')
plt.ylabel('Number of Rentals')
plt.show()
