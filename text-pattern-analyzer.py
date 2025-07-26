import re
from collections import Counter
import matplotlib.pyplot as plt

# Load text file
with open("sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

# Clean text: remove symbols
words = re.findall(r'\b[a-z]{3,}\b', text)

# Word counts
word_freq = Counter(words)

# Pattern: Words starting with 'pre'
pre_words = [w for w in words if w.startswith("pre")]
pre_count = Counter(pre_words)

# Pattern: Words ending in 'ing'
ing_words = [w for w in words if w.endswith("ing")]
ing_count = Counter(ing_words)

# Word length distribution
length_dist = Counter([len(word) for word in words])

# Longest & shortest words
longest = max(words, key=len)
shortest = min(words, key=len)

print(f" Total Words: {len(words)}")
print(f" Unique Words: {len(word_freq)}")
print(f" Longest Word: {longest}")
print(f" Shortest Word: {shortest}")

print(f"\n Words starting with 'pre': {len(pre_words)}")
print(f" Words ending with 'ing': {len(ing_words)}")

# Plotting word length distribution
plt.bar(length_dist.keys(), length_dist.values(), color="skyblue")
plt.xlabel("Word Length")
plt.ylabel("Frequency")
plt.title("Word Length Distribution")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
