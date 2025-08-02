import pandas as pd
import matplotlib.pyplot as plt

# Sample data (in liters)
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Water_Intake': [2.5, 2.0, 3.0, 2.8, 1.9, 2.2, 2.6]
}

df = pd.DataFrame(data)

# Print table
print("\n Weekly Water Intake (Liters):\n")
print(df)

# Plotting the line graph
plt.figure(figsize=(9, 5))
plt.plot(df['Day'], df['Water_Intake'], marker='o', linestyle='-', color='blue')

plt.title(" Daily Water Intake Over a Week")
plt.xlabel("Day")
plt.ylabel("Water Intake (Liters)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Highlight min and max intake days
max_day = df.loc[df['Water_Intake'].idxmax()]
min_day = df.loc[df['Water_Intake'].idxmin()]
plt.annotate(f"Max: {max_day['Water_Intake']}L", (max_day['Day'], max_day['Water_Intake'] + 0.1), color='green')
plt.annotate(f"Min: {min_day['Water_Intake']}L", (min_day['Day'], min_day['Water_Intake'] - 0.3), color='red')

plt.show()
