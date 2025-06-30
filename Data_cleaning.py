# 📌 Step 1: Import pandas
import pandas as pd

# 📌 Step 2: Sample sales data with wrong entries
data = {
    'Transaction_ID': [1, 2, 3, 4, 5],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Mobile', 'Tablet'],
    'Quantity': [2, -1, 3, 1000, 2],  # -1 and 1000 are invalid
    'Price': ['50,000', '20,000', '15,000', '30,000', 'invalid']
}
df = pd.DataFrame(data)

# 📌 Step 3: Display raw data
print("Raw Sales Data:")
print(df)

# ✅ Step 4: Fix quantity errors (remove negative or unrealistic numbers)
df = df[(df['Quantity'] > 0) & (df['Quantity'] < 100)]  # Assuming realistic quantity is < 100

# ✅ Step 5: Remove commas from price and convert to numeric
df['Price'] = df['Price'].str.replace(',', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# ✅ Step 6: Drop rows where price couldn't be converted
df = df.dropna(subset=['Price'])

# 📌 Step 7: Final cleaned sales data
print("\nCleaned Sales Data:")
print(df)
