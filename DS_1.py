# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Note: Download the CSV file from the World Bank and place it in your working directory
# The file is usually named something like: 'API_SP.POP.TOTL_DS2_en_csv_v2_xxxxxx.csv'

# Load only the data sheet (usually the 5th sheet in Excel)
 # Update with your file name

# Step 2: Skip the metadata rows (usually first 4) and load the data
data = pd.read_csv('pop.csv', skiprows=4)

# Step 3: Inspect the structure
print(data.head())

# Step 4: Select columns we need
# We'll extract the latest year's population data — e.g., 2022
# Replace '2022' with the latest year column in your file if different
latest_year = '2022'

# Remove rows with missing population values for the latest year
data_clean = data[['Country Name', latest_year]].dropna()

# Step 5: Convert population to integers
data_clean[latest_year] = data_clean[latest_year].astype(int)

# Step 6: Sort and select the top 10 populous countries
top_10 = data_clean.sort_values(by=latest_year, ascending=False).head(10)

# Step 7: Plotting the bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_10['Country Name'], top_10[latest_year], color='darkcyan')
plt.title(f'Top 10 Most Populous Countries in {latest_year}', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()