import pandas as pd
import matplotlib.pyplot as plt

# Simulated sleep data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Sleep_Hours': [6.5, 7.0, 5.5, 6.0, 8.0, 9.5, 7.5],
    'Sleep_Quality': [6, 7, 5, 6, 8, 9, 7]  # 1 (worst) to 10 (best)
}

df = pd.DataFrame(data)

# Display sleep log
print("\n🛏 Weekly Sleep Log:\n")
print(df)

# Summary statistics
print("\n Summary:")
print(f"Average Sleep Hours: {df['Sleep_Hours'].mean():.2f} hrs")
print(f"Best Sleep Quality: {df.loc[df['Sleep_Quality'].idxmax()]['Day']} ({df['Sleep_Quality'].max()}/10)")
print(f"Worst Sleep Quality: {df.loc[df['Sleep_Quality'].idxmin()]['Day']} ({df['Sleep_Quality'].min()}/10)")

# Line plot - Sleep hours & quality
plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['Sleep_Hours'], marker='o', label='Sleep Hours')
plt.plot(df['Day'], df['Sleep_Quality'], marker='s', label='Sleep Quality', linestyle='--')
plt.title(" Sleep Duration vs Quality Over the Week")
plt.xlabel("Day")
plt.ylabel("Hours / Quality Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
