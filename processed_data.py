import pandas as pd
import glob
import os

# Find all CSV files in the data folder
all_files = glob.glob("data/*.csv")
print(f"Found {len(all_files)} CSV files")

# Combine all CSV files
df_list = []
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)
    print(f"Loaded {file} - {len(df)} rows")

sales_data = pd.concat(df_list, ignore_index=True)
print(f"\nTotal rows before filtering: {len(sales_data)}")

# Filter for only Pink Morsels
pink_morsel = sales_data[sales_data['product'] == 'pink morsel'].copy()
print(f"Rows after filtering for Pink Morsels: {len(pink_morsel)}")

# Clean the price column (remove $ sign)
pink_morsel['price_numeric'] = pink_morsel['price'].replace('[\$,]', '', regex=True).astype(float)

#Create 'sales' field by multiplying quantity and price
pink_morsel['sales'] = pink_morsel['price_numeric'] * pink_morsel['quantity']

#Select only the required columns: Sales, Date, Region
output_data = pink_morsel[['sales', 'date', 'region']].copy()

#Sort by date to make it organized
output_data = output_data.sort_values('date')

# Save to a new CSV file
output_data.to_csv('formatted_output.csv', index=False)
print(f"\nSaved formatted_output.csv with {len(output_data)} rows")
print("\nFirst 5 rows of output:")
print(output_data.head())

print("\nLast 5 rows of output:")
print(output_data.tail())

# Show summary statistics
print("\n" + "="*50)
print("SUMMARY STATISTICS")
print("="*50)
print(f"Total Sales: ${output_data['sales'].sum():,.2f}")
print(f"Date range: {output_data['date'].min()} to {output_data['date'].max()}")
print(f"Regions included: {sorted(output_data['region'].unique())}")