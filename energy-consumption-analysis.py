import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("household_power_consumption.csv", sep=';', low_memory=False)

# Convert date and time
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce')
df = df.dropna(subset=['Datetime'])

# Convert to numeric values
for col in ['Global_active_power', 'Global_reactive_power', 'Voltage']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop NA
df.dropna(inplace=True)

# Plot power usage over time
plt.figure(figsize=(10, 5))
plt.plot(df['Datetime'], df['Global_active_power'], color='red')
plt.title(" Global Active Power Usage Over Time")
plt.xlabel("Time")
plt.ylabel("Global Active Power (kilowatts)")
plt.tight_layout()
plt.show()

# Hourly usage pattern
df['Hour'] = df['Datetime'].dt.hour
sns.boxplot(x='Hour', y='Global_active_power', data=df, palette='coolwarm')
plt.title(" Power Usage by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Power (kW)")
plt.show()
