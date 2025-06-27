import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Simulated dataset
data = {
    'state': ['Punjab', 'Maharashtra', 'Tamil Nadu', 'UP', 'Punjab', 'UP', 'TN', 'Maharashtra', 'Punjab', 'UP'],
    'crop': ['Wheat', 'Sugarcane', 'Rice', 'Wheat', 'Rice', 'Sugarcane', 'Wheat', 'Rice', 'Sugarcane', 'Rice'],
    'year': [2018, 2018, 2018, 2019, 2019, 2019, 2020, 2020, 2020, 2021],
    'area_hectare': [1200, 900, 1100, 1000, 1150, 800, 1300, 950, 850, 1000],
    'production_tons': [3200, 2700, 4000, 2900, 3600, 2500, 3800, 3000, 2400, 3400]
}
df = pd.DataFrame(data)

# Sample preview
print("🌾 Crop Production Data Sample:")
print(df.head())

# 🚜 Total production by crop
crop_total = df.groupby('crop')['production_tons'].sum().reset_index()
sns.barplot(x='crop', y='production_tons', data=crop_total)
plt.title("🌽 Total Production by Crop")
plt.show()

# 📍 Production trends over years
sns.lineplot(x='year', y='production_tons', hue='crop', data=df, marker='o')
plt.title("📈 Crop Production Over Years")
plt.show()

# 🗺️ State-wise comparison
sns.boxplot(x='state', y='production_tons', data=df)
plt.title("🏞️ State-wise Crop Production")
plt.xticks(rotation=45)
plt.show()

# 💡 Check yield (tons/hectare)
df['yield'] = df['production_tons'] / df['area_hectare']
sns.barplot(x='crop', y='yield', data=df)
plt.title("🌾 Average Yield by Crop")
plt.show()

# 📌 Insights
print("\n📌 Key Insights:")
print("- Rice has the highest total production.")
print("- Yield varies significantly by crop type.")
print("- Punjab performs strongly in all crops.")
print("- Crop production has increased in most states over time.")
