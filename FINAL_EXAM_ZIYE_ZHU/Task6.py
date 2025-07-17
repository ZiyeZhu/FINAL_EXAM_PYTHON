import wbdata
import pandas as pd
from datetime import datetime

# ISO country code for Aruba
country = "AW"

# Set the time range: from January 1, 2015 to December 31, 2020
date_range = (datetime(2015, 1, 1), datetime(2020, 12, 31))

# Define the World Bank indicator for total population
indicator = {"SP.POP.TOTL": "Population"}

# Fetch the data from the World Bank
df = wbdata.get_dataframe(indicator, country=country, date=date_range)

# Reset index
df = df.reset_index()

# Convert 'date' column to datetime type so we can extract year
df["date"] = pd.to_datetime(df["date"])

# Sort by year in ascending order
df = df.sort_values(by="date", ascending=True)

# Print header
print("Country | Year | Population")

# Loop through each row and print results
for _, row in df.iterrows():
    year = row["date"].year
    population = int(row["Population"])
    print(f"Aruba | {year} | {population}")