import pandas as pd
import matplotlib.pyplot as plt

# Load time-series CSV
file_path = "time_series_data.csv"  # CSV must have 'Date' and 'Value' columns
df = pd.read_csv(file_path)

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date just in case
df = df.sort_values('Date')

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='blue')
plt.title("Time Series Trend")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
