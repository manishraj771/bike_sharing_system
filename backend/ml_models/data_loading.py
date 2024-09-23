import pandas as pd

# Load the data from the local 'data/' directory
day_data = pd.read_csv('data/day.csv')  
hour_data = pd.read_csv('data/hour.csv')

# Display basic info about the datasets
print(day_data.info())
print(hour_data.info())
