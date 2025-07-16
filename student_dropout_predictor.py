import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv("student_dropout.csv")

# Encode categorical variables
df = pd.get_dummies(df, drop_first=True)

# Features and label
X = df.drop('dropout', axis=1)
y = df['dropout']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict & evaluate
y_pred = model.predict(X_test)
print(" Accuracy:", accuracy_score(y_test, y_pred))
print(" Classification Report:\n", classification_report(y_test, y_pred))

# Visualization
sns.countplot(x='dropout', data=df, palette='Set2')
plt.title(" Dropout Class Distribution")
plt.xticks([0, 1], ['Continued', 'Dropped Out'])
plt.show()
