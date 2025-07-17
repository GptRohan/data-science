import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("youtube_channel_data.csv")

# Convert upload date
df['Upload Date'] = pd.to_datetime(df['Upload Date'])

# Extract month
df['Month'] = df['Upload Date'].dt.month_name()

# Plot most viewed videos
top_views = df.sort_values(by='Views', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Views', y='Video Title', data=top_views, palette='Blues_r')
plt.title("🔥 Top 10 Most Viewed Videos")
plt.xlabel("Views")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()

# Monthly upload count
monthly_uploads = df['Month'].value_counts().reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

monthly_uploads.plot(kind='bar', color='orange', figsize=(10, 5))
plt.title("📅 Monthly Upload Distribution")
plt.xlabel("Month")
plt.ylabel("Number of Videos")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Engagement rate = (Likes + Comments) / Views
df['Engagement Rate'] = (df['Likes'] + df['Comments']) / df['Views']

# Engagement distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Engagement Rate'], bins=30, color='purple')
plt.title("🎯 Engagement Rate Distribution")
plt.xlabel("Engagement Rate")
plt.tight_layout()
plt.show()
