import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_data import load_excel_data  # Make sure this file is in the same folder

# Set a consistent visual style for all plots
sns.set(style="whitegrid")

# Load Excel file and specific sheet
file_path = "../ZHU Ziye.xlsx"
sheet_name = "bank_loans"
df = load_excel_data(file_path, sheet_name)

# -------------------------------
# Plot 6: Histogram of Loan Term
# -------------------------------
# This histogram shows how loan terms (in months) are distributed.
plt.figure(figsize=(10, 6))
sns.histplot(df['Term'], bins=15, kde=False, color='lightgreen')
plt.title("Distribution of Loan Term")
plt.xlabel("Loan Term (Months)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("loan_term_histogram.png")
plt.show()

# --------------------------------------
# Plot 7: Bar Plot of Loan Title Counts
# --------------------------------------
# Visualize the most common purposes for loans, based on 'Loan Title'
plt.figure(figsize=(12, 6))
title_counts = df['Loan Title'].value_counts().head(10)
sns.barplot(x=title_counts.index, y=title_counts.values, palette="coolwarm")
plt.title("Top 10 Loan Titles")
plt.xlabel("Loan Title")
plt.ylabel("Number of Loans")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("loan_title_barplot.png")
plt.show()

# ------------------------------------------------------
# Plot 8: Stacked Bar Plot of Loan Status by Loan Title
# ------------------------------------------------------
# Show how loan status (e.g. Fully Paid, Charged Off) varies by loan purpose
loan_status_by_title = df.pivot_table(index='Loan Title', columns='Loan Status', aggfunc='size', fill_value=0)
loan_status_by_title = loan_status_by_title.loc[
    loan_status_by_title.sum(axis=1).sort_values(ascending=False).head(10).index
]
loan_status_by_title.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set2')
plt.title("Loan Status by Loan Title (Top 10)")
plt.xlabel("Loan Title")
plt.ylabel("Number of Loans")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("loan_status_by_title_stackedbar.png")
plt.show()