import pandas as pd

# Extract: Load raw banking transaction data
df = pd.read_csv("data/bank_transactions.csv")

print("Original Dataset")
print(df)

# Transform: Remove duplicated transaction IDs
df = df[~df["Transaction_ID"].duplicated(keep=False)]

# Transform: Remove rows with missing customer IDs
df = df.dropna(subset=["Customer_ID"])

# Transform: Remove negative transaction amounts
df = df[df["Amount"] > 0]

# Transform: Keep only completed transactions
df = df[df["Status"] == "Completed"]

# Load: Save cleaned dataset
df.to_csv("output/clean_bank_transactions.csv", index=False)

print("Clean dataset saved successfully")
print(df)
