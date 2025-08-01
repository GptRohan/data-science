import pandas as pd
import matplotlib.pyplot as plt

# Expense data for the month
data = {
    'Category': ['Rent', 'Groceries', 'Transport', 'Internet', 'Utilities', 'Entertainment', 'Miscellaneous'],
    'Amount': [12000, 4500, 1600, 1000, 1500, 3000, 2000]
}

df = pd.DataFrame(data)

# Display data
print("\n Monthly Expenses Table:\n")
print(df)

# Bar chart + line chart
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Amount'], color='skyblue', label='Amount Spent')
plt.plot(df['Category'], df['Amount'], color='red', marker='o', label='Trend')

plt.title(" Monthly Expenses by Category")
plt.xlabel("Expense Category")
plt.ylabel("Amount (INR)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show chart
plt.show()
