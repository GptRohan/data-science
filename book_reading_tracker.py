import pandas as pd
import matplotlib.pyplot as plt

# Simulated book data
data = {
    'Book': [
        'The Power of Habit', 'Atomic Habits', 'Deep Work',
        'Ikigai', 'Start With Why', 'Grit', 'The Alchemist'
    ],
    'Pages_Read': [320, 280, 300, 190, 250, 270, 180],
    'Rating': [8, 9, 8.5, 7, 9, 8, 9.5]  # Rating out of 10
}

df = pd.DataFrame(data)

# Display reading log
print("\n Book Reading Log:\n")
print(df)

# Summary stats
avg_pages = df['Pages_Read'].mean()
highest_rated = df.loc[df['Rating'].idxmax()]

print(f"\n Average Pages per Book: {avg_pages:.2f}")
print(f" Favorite Book: '{highest_rated['Book']}' (Rating: {highest_rated['Rating']}/10)")

# Plotting pages vs rating
plt.figure(figsize=(10, 5))
plt.scatter(df['Pages_Read'], df['Rating'], color='purple', s=100)

for i in range(len(df)):
    plt.text(df['Pages_Read'][i]+2, df['Rating'][i], df['Book'][i], fontsize=8)

plt.title(" Pages Read vs Book Rating")
plt.xlabel("Pages Read")
plt.ylabel("Rating (out of 10)")
plt.grid(True)
plt.tight_layout()
plt.show()
