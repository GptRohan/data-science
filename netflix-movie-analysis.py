# netflix_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Display first few records
print("📄 Dataset preview:")
print(df.head())

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year

# Count of content type
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('📺 Content Type Distribution (Movies vs TV Shows)')
plt.show()

# Top 10 genres
plt.figure(figsize=(10,5))
df['listed_in'].str.split(',').explode().str.strip().value_counts().head(10).plot(kind='bar', color='tomato')
plt.title('🎬 Top 10 Genres on Netflix')
plt.ylabel('Number of Titles')
plt.show()

# Trend of content added over years
df['year_added'].value_counts().sort_index().plot(kind='line', marker='o', color='green', figsize=(8,5))
plt.title('🕰️ Content Added Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.show()
