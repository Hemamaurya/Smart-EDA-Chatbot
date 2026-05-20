import pandas as pd
import numpy as np

# Step 1: Raw data load karo
print("=== Raw Data Loading ===")
df = pd.read_csv("HRDataset_v14.csv")
print(f"Shape: {df.shape}")
print(f"\nColumn names:\n{df.columns.tolist()}")
print(f"\nPehli 3 rows:\n{df.head(3)}")

# Step 2: Missing values dekhlo
print("\n=== Missing Values ===")
missing = df.isnull().sum()
print(missing[missing > 0])

# Step 3: Data types dekhlo
print("\n=== Data Types ===")
print(df.dtypes)

# Step 4: Duplicate rows hataao
print(f"\n=== Duplicates ===")
print(f"Duplicate rows before: {df.duplicated().sum()}")
df = df.drop_duplicates()
print(f"Duplicate rows after: {df.duplicated().sum()}")

# Step 5: Column names clean karo (spaces hataao)
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
print(f"\nCleaned column names:\n{df.columns.tolist()}")

# Step 6: Missing values handle karo
# Numeric columns mein median bharo
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    null_count = df[col].isnull().sum()
    if null_count > 0:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
        print(f"{col}: {null_count} nulls filled with median {median_val:.2f}")

# Text columns mein 'Unknown' bharo
text_cols = df.select_dtypes(include=['object']).columns
for col in text_cols:
    null_count = df[col].isnull().sum()
    if null_count > 0:
        df[col].fillna("Unknown", inplace=True)
        print(f"{col}: {null_count} nulls filled with 'Unknown'")

# Step 7: Date columns fix karo
date_cols = [col for col in df.columns if 'date' in col.lower()]
for col in date_cols:
    try:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        print(f"{col}: converted to datetime")
    except:
        print(f"{col}: conversion failed, skipping")

# Step 8: Salary column clean karo (agar $ ya comma ho)
if 'pay_rate' in df.columns:
    df['pay_rate'] = pd.to_numeric(df['pay_rate'], errors='coerce')
    print("\nPay rate cleaned")

# Step 9: Final check
print("\n=== Final Data Info ===")
print(f"Shape: {df.shape}")
print(f"Missing values remaining:\n{df.isnull().sum()[df.isnull().sum() > 0]}")

# Step 10: Clean data save karo
df.to_csv("hr_data_clean.csv", index=False)
print("\n✓ Clean data saved as hr_data_clean.csv")