# Plot2_Boxplot_Loan_Status.py
import matplotlib.pyplot as plt
import seaborn as sns
from load_data import load_excel_data  # Import the data loading function

# Set visual style for plots
sns.set(style="whitegrid")

# Step 1: Define the file path and sheet name
file_path = "../ZHU Ziye.xlsx"
sheet_name = "bank_loans"

# Step 2: Load the data
df = load_excel_data(file_path, sheet_name)

# Step 3: Create a boxplot to compare Loan Amount by Loan Status
plt.figure(figsize=(10, 6))
sns.boxplot(x='Loan Status', y='Loan Amount', data=df, palette='pastel')
plt.title("Loan Amount by Loan Status")
plt.xlabel("Loan Status")
plt.ylabel("Loan Amount")
plt.tight_layout()
plt.savefig("Boxplot_Loan_Status.png")
plt.show()