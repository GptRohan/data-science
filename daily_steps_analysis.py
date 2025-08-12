import pandas as pd
import matplotlib.pyplot as plt

# Sample step count data
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Steps': [4500, 6700, 5800, 7200, 8000, 9500, 5000]
}

df = pd.DataFrame(data)

# Display data
print("\n Weekly Step Count:\n")
print(df)

# Summary statistics
total_steps = df['Steps'].sum()
avg_steps = df['Steps'].mean()
max_day = df.loc[df['Steps'].idxmax()]
min_day = df.loc[df['Steps'].idxmin()]

print(f"\n Total Weekly Steps: {total_steps} steps")
print(f" Average Daily Steps: {avg_steps:.2f} steps")
print(f" Highest Activity Day: {max_day['Day']} ({max_day['Steps']} steps)")
print(f" Lowest Activity Day: {min_day['Day']} ({min_day['Steps']} steps)")

# Visualization - Line Chart
plt.figure(figsize=(8, 5))
plt.plot(df['Day'], df['Steps'], marker='o', linestyle='-', color='green')

plt.title(" Weekly Step Count Trend")
plt.xlabel("Day")
plt.ylabel("Steps Walked")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
