import pandas as pd
import glob
import os

# Load all CSV files from the data folder
all_files = glob.glob("data/*.csv")
print(f"Found {len(all_files)} CSV files")

# Combine all CSV files
df_list = []
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)

sales_data = pd.concat(df_list, ignore_index=True)

# Filter for pink morsel only
pink_morsel = sales_data[sales_data['product'] == 'pink morsel'].copy()

# Clean the price column (remove $ sign and convert to float)
pink_morsel['price_numeric'] = pink_morsel['price'].replace('[\$,]', '', regex=True).astype(float)

# Calculate sales (price * quantity)
pink_morsel['sales'] = pink_morsel['price_numeric'] * pink_morsel['quantity']

# Convert date to datetime
pink_morsel['date'] = pd.to_datetime(pink_morsel['date'])

# Split data before and after Jan 15, 2021
before_date = '2021-01-15'
after_date = '2021-01-15'

before = pink_morsel[pink_morsel['date'] < before_date]
after = pink_morsel[pink_morsel['date'] >= after_date]

# Calculate total sales
total_before = before['sales'].sum()
total_after = after['sales'].sum()

# Print results
print("\n" + "="*50)
print("PINK MORSEL SALES ANALYSIS")
print("="*50)
print(f"Date range in data: {pink_morsel['date'].min()} to {pink_morsel['date'].max()}")
print(f"\nTotal sales BEFORE price increase: ${total_before:,.2f}")
print(f"Total sales AFTER price increase: ${total_after:,.2f}")

if total_after > total_before:
    print(f"\nSales were HIGHER after the price increase by ${total_after - total_before:,.2f}")
elif total_before > total_after:
    print(f"\nSales were HIGHER before the price increase by ${total_before - total_after:,.2f}")
else:
    print("\nSales were the same before and after")

# Additional analysis - daily average sales
print("\n" + "="*50)
print("DAILY AVERAGE SALES")
print("="*50)
print(f"Before: ${before['sales'].mean():,.2f} per day")
print(f"After: ${after['sales'].mean():,.2f} per day")