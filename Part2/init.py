import pandas as pd
from load_data import load_excel_data

# Step 1: Set the file path and sheet name
file_path = "../ZHU Ziye.xlsx"
sheet_name = "bank_loans"  # Update if your sheet name is different

# Step 2: Load the data
df = load_excel_data(file_path, sheet_name)

# Step 3: Preview data
print(df.head())

# Step 4: Get basic info (column types, non-null counts)
print("\nBasic DataFrame Info:")
print(df.info())

# Step 5: Get statistical summary for numerical columns
print("\nStatistical Summary:")
print(df.describe())

# Step 6: Check for missing values in each column
print("\nMissing Values (per column):")
print(df.isnull().sum())

# Step 7: List all column names
print("\nColumn Names:")
print(df.columns.tolist())

# Step 8: Check data types
print("\nData Types:")
print(df.dtypes)

# Check for fully duplicated rows
duplicate_rows = df[df.duplicated()]
if duplicate_rows.empty:
    print("✅ No fully duplicated rows found in the dataset.")
else:
    print("⚠️ Found duplicated rows:")
    print(duplicate_rows)

print("Available columns:", df.columns.tolist())

# Define the column you want to check as a potential index
id_column = "ID"  # Replace with the actual column name if different
# Step 1: Check if the column contains any duplicate values
if df[id_column].duplicated().any():
    print(f"❌ The column '{id_column}' contains duplicate values and cannot be used as an index.")
else:
    print(f"✅ The column '{id_column}' is unique. It can be safely used as an index.")

    # Step 2: Set the column as the index of the DataFrame
    df.set_index(id_column, inplace=True)
    print("✔️ Successfully set as index.")
