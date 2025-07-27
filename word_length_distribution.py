from collections import Counter
import matplotlib.pyplot as plt
import re

# Load text from file (or paste your own string here)
file_path = "sample_text.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read().lower()

# Remove special characters, keep only words
words = re.findall(r'\b\w+\b', text)

# Count word lengths
length_counts = Counter(len(word) for word in words)

# Print word length frequency
print(" Word Length Frequency:")
for length, count in sorted(length_counts.items()):
    print(f"Length {length}: {count} words")

# Plot
lengths = list(length_counts.keys())
counts = list(length_counts.values())

plt.figure(figsize=(10, 5))
plt.bar(lengths, counts, color='teal')
plt.xlabel("Word Length")
plt.ylabel("Number of Words")
plt.title("Distribution of Word Lengths in Text")
plt.grid(True, axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
