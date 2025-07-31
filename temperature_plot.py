import pandas as pd
import matplotlib.pyplot as plt

# Load the temperature data
df = pd.read_csv("weekly_temperature.csv")

# Display the dataset
print("\n Weekly Temperature Data:\n")
print(df)

# Plotting the temperature trend
plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['Temperature'], marker='o', linestyle='-', color='orange')
plt.title("Daily Temperature Trend Over a Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
