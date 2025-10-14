# Simple NLP example in Python

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Natural Language Processing with Python is interesting and powerful."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Remove stopwords
filtered_words = [word for word in tokens if word.lower() not in stopwords.words('english')]
print("After stopword removal:", filtered_words)

# Stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]
print("After stemming:", stemmed_words)