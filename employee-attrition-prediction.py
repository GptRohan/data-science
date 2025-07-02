import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load the dataset
df = pd.read_csv("employee_data.csv")

# Encode categorical features
le = LabelEncoder()
df['Attrition'] = le.fit_transform(df['Attrition'])  # Yes = 1, No = 0
df['OverTime'] = le.fit_transform(df['OverTime'])

# Select relevant features
features = ['Age', 'MonthlyIncome', 'DistanceFromHome', 'OverTime', 'JobSatisfaction']
X = df[features]
y = df['Attrition']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Classification Report:\n", classification_report(y_test, y_pred))
print("🔍 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
