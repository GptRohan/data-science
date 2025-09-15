# ===============================
# 📊 EDA on Gallstone Dataset
# ===============================

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load the dataset
# -------------------------------
# Replace with your file name, e.g., gallstone.csv
df = pd.read_csv("gallstone.csv")

# Quick preview of the data
print("🔍 Shape of dataset:", df.shape)
print("\n👀 First 5 rows:\n", df.head())

# -------------------------------
# 2. Basic information
# -------------------------------
print("\n📌 Dataset Info:")
print(df.info())

# Check missing values
print("\n❓ Missing values:\n", df.isnull().sum())

# Summary statistics for numerical columns
print("\n📊 Summary statistics:\n", df.describe())

# Unique values in categorical columns
print("\n🔑 Unique values in categorical columns:")
for col in df.select_dtypes(include=["object"]).columns:
    print(f"{col}: {df[col].unique()}")

# -------------------------------
# 3. Target Variable Analysis
# -------------------------------
if "Gallstones" in df.columns:   # assuming target column is 'Gallstones' (Yes/No)
    sns.countplot(data=df, x="Gallstones")
    plt.title("Distribution of Gallstones (Target Variable)")
    plt.show()

# -------------------------------
# 4. Correlation Heatmap
# -------------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap (Numerical Features)")
plt.show()

# -------------------------------
# 5. Distribution of Numerical Features
# -------------------------------
df.hist(figsize=(12, 8), bins=20, edgecolor="black")
plt.suptitle("Feature Distributions", size=16)
plt.show()

# -------------------------------
# 6. Boxplots to Check Outliers
# -------------------------------
plt.figure(figsize=(12,6))
sns.boxplot(data=df.select_dtypes(include=np.number))
plt.title("Boxplot of Numerical Features")
plt.show()

# -------------------------------
# 7. Relationships
# -------------------------------
# Age vs Gallstones
if "Age" in df.columns and "Gallstones" in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x="Age", hue="Gallstones", multiple="stack", kde=True)
    plt.title("Age vs Gallstone Occurrence")
    plt.show()

# Gender vs Gallstones
if "Gender" in df.columns and "Gallstones" in df.columns:
    sns.countplot(data=df, x="Gender", hue="Gallstones")
    plt.title("Gender vs Gallstone Occurrence")
    plt.show()

# BMI vs Gallstones
if "BMI" in df.columns and "Gallstones" in df.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x="Gallstones", y="BMI")
    plt.title("BMI vs Gallstone Occurrence")
    plt.show()

# Pain Level vs Gallstones
if "PainLevel" in df.columns and "Gallstones" in df.columns:
    sns.countplot(data=df, x="PainLevel", hue="Gallstones")
    plt.title("Pain Level vs Gallstone Occurrence")
    plt.show()