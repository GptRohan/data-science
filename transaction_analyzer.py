import pandas as pd
import matplotlib.pyplot as plt

# Simulated transaction data
data = {
    "Customer_ID": ["C001", "C002", "C001", "C003", "C002", "C004", "C003", "C001"],
    "Transaction_Type": ["Deposit", "Withdrawal", "Deposit", "Withdrawal", "Deposit", "Deposit", "Deposit", "Withdrawal"],
    "Amount": [5000, 2000, 3000, 1500, 6000, 4000, 1000, 2500]
}

df = pd.DataFrame(data)

# Total amounts by type
totals = df.groupby("Transaction_Type")["Amount"].sum()
print(" Total Amounts:")
print(totals)

# Average transaction
avg_transaction = df["Amount"].mean()
print(f"\n Average Transaction Amount: ₹{avg_transaction:.2f}")

# Most active customer (most number of transactions)
most_active = df["Customer_ID"].value_counts().idxmax()
print(f"\n Most Active Customer: {most_active}")

# Bar chart of total deposits vs withdrawals
totals.plot(kind="bar", color=["green", "red"])
plt.title("Total Deposit vs Withdrawal")
plt.ylabel("Amount (₹)")
plt.tight_layout()
plt.show()
