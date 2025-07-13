import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("loan_data.csv")

# Encode categorical features
df = pd.get_dummies(df, drop_first=True)

# Separate features and label
X = df.drop('loan_default', axis=1)
y = df['loan_default']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(" Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Visualize: default rate by income
sns.boxplot(x='loan_default', y='annual_income', data=df)
plt.title(" Annual Income vs Loan Default")
plt.xticks([0, 1], ["No Default", "Default"])
plt.show()
