import pandas as pd

# -----------------------------
# Step 1: Load your data
# -----------------------------
df = pd.read_csv("data.csv")   # change file name if needed

# -----------------------------
# Step 2: Store basic summary
# -----------------------------
summary = pd.DataFrame({
    "column_name": df.columns,
    "data_type": df.dtypes.astype(str),
    "total_rows": len(df),
    "null_count": df.isnull().sum().values,
    "unique_count": df.nunique().values,
    "mean": df.mean(numeric_only=True).reindex(df.columns).values,
    "median": df.median(numeric_only=True).reindex(df.columns).values,
    "std": df.std(numeric_only=True).reindex(df.columns).values,
    "min_val": df.min(numeric_only=True).reindex(df.columns).values,
    "max_val": df.max(numeric_only=True).reindex(df.columns).values
})

# Save to CSV
summary.to_csv("eda_summary.csv", index=False)

# -----------------------------
# Step 3: Value counts for each column
# -----------------------------
value_counts = []
for col in df.columns:
    vc = df[col].value_counts(normalize=True, dropna=False).reset_index()
    vc.columns = ["value", "percentage"]
    vc["column_name"] = col
    vc["count"] = df[col].value_counts(dropna=False).values
    value_counts.append(vc)

value_counts = pd.concat(value_counts)
value_counts.to_csv("eda_value_counts.csv", index=False)

# -----------------------------
# Step 4: Correlation matrix
# -----------------------------
corr = df.corr(numeric_only=True)
corr.to_csv("eda_correlations.csv")

print("✅ EDA results stored as CSV files (eda_summary.csv, eda_value_counts.csv, eda_correlations.csv)")