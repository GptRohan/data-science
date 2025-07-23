import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# User input: Webpage URL
url = input("Enter a webpage URL: ")

# Fetch the web page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract visible text only
for script in soup(['script', 'style']):
    script.extract()

text = soup.get_text()
words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())

# Remove common stopwords (custom list)
stopwords = set(["the", "and", "for", "are", "that", "this", "with", "was", "from", "you", "have", "your", "not"])
filtered_words = [word for word in words if word not in stopwords]

# Count word frequency
word_counts = Counter(filtered_words)
top_words = word_counts.most_common(10)

print("\n Top 10 Most Frequent Words:")
for word, count in top_words:
    print(f"{word}: {count} times")
