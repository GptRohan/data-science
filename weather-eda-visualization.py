import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the weather dataset
df = pd.read_csv("daily_weather.csv")  # Replace with actual path or dataset

# Preview the data
print("📄 Weather dataset preview:")
print(df.head())

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Add year and month columns
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Line plot of temperature over time
plt.figure(figsize=(12, 5))
sns.lineplot(x='date', y='temperature_max', data=df)
plt.title("🌡️ Daily Maximum Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Max Temp (°C)")
plt.grid(True)
plt.show()

# Rainfall distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['precipitation'], bins=30, kde=True, color='skyblue')
plt.title("🌧️ Rainfall Distribution")
plt.xlabel("Precipitation (mm)")
plt.ylabel("Frequency")
plt.show()

# Average monthly temperature
monthly_avg = df.groupby('month')['temperature_max'].mean()
monthly_avg.plot(kind='bar', color='coral', figsize=(8,5))
plt.title("📆 Average Monthly Max Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()
