import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("student-mat.csv", sep=';')

# Create a binary target
df['pass'] = df['G3'].apply(lambda x: 1 if x >= 10 else 0)

# Select features
features = ['studytime', 'failures', 'absences', 'G1', 'G2']
X = df[features]
y = df['pass']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print(" Accuracy:", accuracy_score(y_test, y_pred))
print(" Classification Report:\n", classification_report(y_test, y_pred))

# Visualize
sns.countplot(x='pass', data=df)
plt.title(" Pass vs Fail Distribution")
plt.xticks([0, 1], ['Fail', 'Pass'])
plt.show()
