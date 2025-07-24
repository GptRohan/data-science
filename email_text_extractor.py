import email
import re
from email import policy
from email.parser import BytesParser
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load .eml file
with open("sample_email.eml", "rb") as file:
    msg = BytesParser(policy=policy.default).parse(file)

# Extract subject and sender
subject = msg["subject"]
sender = msg["from"]

# Extract email body
body = ""
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body += part.get_content()
else:
    body = msg.get_content()

# Clean the body
text = re.sub(r'\W+', ' ', body.lower())
filtered = [word for word in text.split() if word not in stop_words]

print(f" Subject: {subject}")
print(f" From: {sender}")
print("\n Cleaned Email Body Preview:")
print(" ".join(filtered[:100]))  # preview first 100 words
