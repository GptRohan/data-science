import pandas as pd
import matplotlib.pyplot as plt

# Simulated mood and weather data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Weather': ['Rainy', 'Cloudy', 'Sunny', 'Sunny', 'Rainy', 'Cloudy', 'Sunny'],
    'Mood_Score': [4, 5, 8, 9, 3, 6, 9]  # Mood score from 1 (bad) to 10 (great)
}

df = pd.DataFrame(data)

# Print data
print("\n🌤 Mood vs Weather Data:\n")
print(df)

# Count mood average for each weather type
weather_mood_avg = df.groupby('Weather')['Mood_Score'].mean().reset_index()

print("\n Average Mood Score by Weather Type:\n")
print(weather_mood_avg)

# Bar plot of weather vs average mood score
plt.figure(figsize=(8, 5))
plt.bar(weather_mood_avg['Weather'], weather_mood_avg['Mood_Score'], color='skyblue')
plt.title(" Average Mood Score by Weather Type")
plt.xlabel("Weather")
plt.ylabel("Average Mood Score")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
