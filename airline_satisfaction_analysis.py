import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("airline_passenger_data.csv")

# Preview data
print(df.head())

# Count of satisfied vs dissatisfied passengers
plt.figure(figsize=(6, 4))
sns.countplot(x='Satisfaction', data=df, palette='Set2')
plt.title(" Passenger Satisfaction Count")
plt.xlabel("Satisfaction Level")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

# Average ratings by satisfaction group
rating_features = ['Seat Comfort', 'Inflight Service', 'Food and Drink']
avg_ratings = df.groupby('Satisfaction')[rating_features].mean()

avg_ratings.plot(kind='bar', figsize=(8,5), colormap='coolwarm')
plt.title(" Average Ratings by Satisfaction Group")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

# Flight distance vs satisfaction
plt.figure(figsize=(8, 5))
sns.boxplot(x='Satisfaction', y='Flight Distance', data=df, palette='pastel')
plt.title(" Flight Distance vs Satisfaction")
plt.tight_layout()
plt.show()

# Correlation heatmap
correlation_data = df[['Seat Comfort', 'Inflight Service', 'Food and Drink', 'Flight Distance', 'Arrival Delay']]
plt.figure(figsize=(7, 5))
sns.heatmap(correlation_data.corr(), annot=True, cmap='Blues')
plt.title(" Correlation Heatmap of Travel Features")
plt.tight_layout()
plt.show()
