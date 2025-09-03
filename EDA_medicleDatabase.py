# Importing important libraries for data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (replace 'medical.csv' with your dataset file)
df = pd.read_csv("medical.csv")

# First look at the dataset
print("Shape of dataset:", df.shape)   # rows, columns
print("\nFirst 5 rows:\n", df.head())  # quick preview

# Basic information about columns
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing values per column:\n", df.isnull().sum())

# Basic statistical summary
print("\nSummary statistics:\n", df.describe())

# Checking unique values in categorical columns (to understand categories)
for col in df.select_dtypes(include=['object']).columns:
    print(f"\nUnique values in {col}:", df[col].unique())

# Distribution of target column (example: disease/no disease)
if "target" in df.columns:
    sns.countplot(data=df, x="target")
    plt.title("Target Variable Distribution")
    plt.show()

# Correlation heatmap (to see relation between numeric features)
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Histogram for all numerical features
df.hist(figsize=(12, 8), bins=20)
plt.suptitle("Feature Distributions")
plt.show()

# Boxplot to check outliers in numerical features
plt.figure(figsize=(12, 6))
sns.boxplot(data=df.select_dtypes(include=[np.number]))
plt.title("Boxplot for Numerical Features")
plt.show()

# Relationship between age and disease (example analysis)
if "age" in df.columns and "target" in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x="age", hue="target", kde=True, multiple="stack")
    plt.title("Age vs Disease Distribution")
    plt.show()
