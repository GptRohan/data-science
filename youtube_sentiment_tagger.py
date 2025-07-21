import pandas as pd
import re

# Load dataset
df = pd.read_csv("youtube_comments.csv")

# Preview
print(" Sample Comments:")
print(df.head())

# Define keywords for simple sentiment detection
positive_words = ['good', 'great', 'awesome', 'fantastic', 'love', 'excellent', 'amazing', 'nice', 'super']
negative_words = ['bad', 'worst', 'hate', 'awful', 'boring', 'terrible', 'poor', 'dislike']
neutral_words = ['ok', 'fine', 'average', 'meh', 'normal']

# Function to tag sentiment
def tag_sentiment(comment):
    comment = str(comment).lower()
    pos = sum(word in comment for word in positive_words)
    neg = sum(word in comment for word in negative_words)
    neu = sum(word in comment for word in neutral_words)

    if pos > neg and pos > neu:
        return 'Positive'
    elif neg > pos and neg > neu:
        return 'Negative'
    else:
        return 'Neutral'

# Apply tagging
df['Sentiment'] = df['Comment'].apply(tag_sentiment)

# Output result
print("\n Tagged Comments:")
print(df[['Comment', 'Sentiment']].head())

# Save to CSV
df.to_csv("tagged_youtube_comments.csv", index=False)
print("\n Output saved to 'tagged_youtube_comments.csv'")
