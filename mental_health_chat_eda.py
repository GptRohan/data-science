import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("mental_health_chat.csv")

# Basic cleanup
df.dropna(subset=['message', 'sentiment'], inplace=True)

# Sentiment distribution
sns.countplot(x='sentiment', data=df, palette='Set2')
plt.title("😊 Sentiment Distribution in Mental Health Chats")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# Message length analysis
df['message_length'] = df['message'].apply(len)
sns.boxplot(x='sentiment', y='message_length', data=df)
plt.title("✍️ Message Length by Sentiment")
plt.show()
