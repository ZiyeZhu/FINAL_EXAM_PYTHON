import matplotlib.pyplot as plt
import seaborn as sns
from load_data import load_excel_data  # 不加 Part2

# Set visual style
sns.set(style="whitegrid")

# Step 1: Load the data
file_path = "../ZHU Ziye.xlsx"
sheet_name = "bank_loans"
df = load_excel_data(file_path, sheet_name)

# Step 2: Plot histogram of Loan Amount
plt.figure(figsize=(10, 6))
sns.histplot(df['Loan Amount'], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Loan Amount")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Histogram_Loan_Amount.png")
plt.show()