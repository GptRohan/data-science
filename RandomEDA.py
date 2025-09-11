# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Create a random dataset
# -----------------------------
np.random.seed(42)  # for reproducibility

df = pd.DataFrame({
    "Age": np.random.randint(18, 70, 100),                 # random ages
    "BloodPressure": np.random.randint(80, 180, 100),       # random BP
    "Cholesterol": np.random.randint(150, 300, 100),        # random cholesterol
    "Gender": np.random.choice(["Male", "Female"], 100),    # random genders
    "Smoker": np.random.choice(["Yes", "No"], 100),         # smoking habit
    "Disease": np.random.choice([0, 1], 100)                # target variable (0 = No, 1 = Yes)
})

print("🔍 First 5 rows:\n", df.head())

# -----------------------------
# 2. EDA
# -----------------------------

# Shape and info
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())

# Missing values
print("\nMissing values:\n", df.isnull().sum())

# Summary statistics
print("\nSummary statistics:\n", df.describe())

# Distribution of target variable
sns.countplot(data=df, x="Disease")
plt.title("Target Distribution (Disease)")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Histograms for numeric columns
df.hist(figsize=(12, 8), bins=15, edgecolor="black")
plt.suptitle("Feature Distributions", size=16)
plt.show()

# Boxplot to check outliers
plt.figure(figsize=(10,6))
sns.boxplot(data=df[["Age","BloodPressure","Cholesterol"]])
plt.title("Boxplot for Numeric Features")
plt.show()

# Relationship between Age and Disease
plt.figure(figsize=(8,5))
sns.histplot(data=df, x="Age", hue="Disease", kde=True, multiple="stack")
plt.title("Age vs Disease Distribution")
plt.show()

# Gender vs Disease
sns.countplot(data=df, x="Gender", hue="Disease")
plt.title("Gender vs Disease")
plt.show()

# Smoker vs Disease
sns.countplot(data=df, x="Smoker", hue="Disease")
plt.title("Smoker vs Disease")
plt.show()