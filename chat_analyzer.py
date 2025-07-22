import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter

# Read chat file
with open("chat.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Extract data from lines (WhatsApp-like format: "12/07/2025, 9:34 AM - Tejas: Hello!")
data = []
pattern = re.compile(r"(\d{2}/\d{2}/\d{4}),\s(\d{1,2}:\d{2})\s(AM|PM)\s-\s(.+?):\s(.*)")

for line in lines:
    match = pattern.match(line)
    if match:
        date, time, meridiem, user, message = match.groups()
        data.append([date, time + ' ' + meridiem, user, message])

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "Time", "User", "Message"])
print(" Preview of parsed messages:")
print(df.head())

# Most active users
user_counts = df['User'].value_counts()
print("\n Most Active Users:")
print(user_counts)

# Plot top 5 active users
user_counts.head(5).plot(kind='bar', color='skyblue')
plt.title("Top 5 Active Users")
plt.ylabel("Number of Messages")
plt.xlabel("User")
plt.tight_layout()
plt.show()

# Word frequency
all_messages = ' '.join(df['Message'].tolist()).lower()
words = re.findall(r'\b\w+\b', all_messages)
common_words = Counter(words).most_common(10)

print("\n Top 10 Most Common Words:")
for word, freq in common_words:
    print(f"{word}: {freq}")

# Convert to DataFrame for plotting
word_df = pd.DataFrame(common_words, columns=['Word', 'Frequency'])
word_df.plot(x='Word', y='Frequency', kind='bar', color='orange', legend=False)
plt.title("Top 10 Words Used in Chat")
plt.tight_layout()
plt.show()
