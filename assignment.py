import pandas as pd
import json
from pandas import ExcelWriter
import xlsxwriter

sales = pd.read_csv('sales.csv')
cust = pd.read_excel('customers.xlsx', sheet_name='customer_info')

try:
    with open('products.json', 'r') as file:
        data = json.load(file)
        prod = pd.json_normalize(data)
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")

# Extract the specified columns
extracted_sales = sales[['transaction_id', 'product_id', 'total_amount']]

#Filter the sales DataFrame to include only transactions where the total_amount is greater than $100
filtered = extracted_sales[extracted_sales['total_amount'] > 100]

#Group the sales data by product_id and 
#calculate the total quantity sold and 
#the average total_amount for each product.
grouped_data = sales.groupby('product_id').agg(
    total_quantity_sold=('quantity', 'sum'),
    average_total_amount=('total_amount', 'mean')
).reset_index()

#Perform an inner join between the sales DataFrame and 
#the products DataFrame on the product_id column to include product details in the sales data.
merged = pd.merge(sales, prod, on='product_id', how='inner')

#Perform a left join between the resulting DataFrame and 
#the customers DataFrame on the customer_id column to include customer details.
lmerged = pd.merge(merged, cust, on='customer_id', how='left')

#Identify and handle any null values in the merged DataFrame by either filling them 
#with default values or dropping rows/columns with missing data.

isnull_values = lmerged.isnull().sum()
fill_null = lmerged.fillna(0)

#Write the cleaned and merged DataFrame to a new CSV file named merged_sales_data.csv.
fill_null.to_csv('merged_sales_data.csv', index=False)

#Replace any negative quantity values with zero in the sales data.
replaced_data = fill_null[fill_null['quantity'] < 0] = 0

#Create a new DataFrame containing only the customer_id, name, and total_amount columns.
new_df = fill_null[['customer_id', 'name', 'total_amount']]

#Convert the product_name column from the products DataFrame into a list.
product_names_list = prod['product_name'].tolist()

#Loop over the total_amount column in the sales DataFrame and calculate the total revenue.
total_revenue = 0
for amount in sales['total_amount']:
    total_revenue += amount

#Parse the products.json file to extract and flatten the nested product details into a usable DataFrame format.
with open('products.json', 'r') as file:
        data = json.load(file)
        prod = pd.json_normalize(data)

#Define a function that categorizes transactions as "High" or "Low" 
#based on the total_amount and apply it to the sales DataFrame, 
#creating a new transaction_category column.
def categorize_transaction(amount):
    if amount >= 100:
        return 'High'
    else:
        return 'Low'
sales['transaction_category'] = sales['total_amount'].apply(categorize_transaction)

#Use loc to select all transactions from a specific region in the customers DataFrame.
filtered_customers = cust.loc[cust['region'] == 'North']

#Use iloc to select the first 10 rows of the merged DataFrame.
first_10_rows = lmerged.iloc[:10]

#Implement a try-except-finally block around the file reading operations to handle potential errors, such as file not found or incorrect file format

# File paths
csv_file = 'sales.csv'
excel_file = 'customers.xlsx'
json_file = 'products.json'

# Reading CSV file
try:
    sales = pd.read_csv(csv_file)
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{csv_file}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{csv_file}' is empty.")
except pd.errors.ParserError:
    print(f"Error: The file '{csv_file}' could not be parsed.")
except Exception as e:
    print(f"An unexpected error occurred while reading the CSV file: {e}")
finally:
    # Optional cleanup actions for CSV file
    print("Finished attempting to read CSV file.")

# Reading Excel file
try:
    cust = pd.read_excel(excel_file, sheet_name='customer_info')
    print("Excel file loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{excel_file}' was not found.")
except ValueError:
    print(f"Error: The sheet 'customer_info' was not found in '{excel_file}'.")
except Exception as e:
    print(f"An unexpected error occurred while reading the Excel file: {e}")
finally:
    # Optional cleanup actions for Excel file
    print("Finished attempting to read Excel file.")

# Reading JSON file
try:
    with open(json_file, 'r') as file:
        data = json.load(file)
    print("JSON file loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{json_file}' was not found.")
except json.JSONDecodeError:
    print(f"Error: The file '{json_file}' could not be decoded. It may not be valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred while reading the JSON file: {e}")
finally:
    # Optional cleanup actions for JSON file
    print("Finished attempting to read JSON file.")


#Write the final processed DataFrame to an Excel file named final_sales_report.xlsx, 
#creating separate sheets for sales data, customer details, and product summaries.

excel_path = 'final_sales_report.xlsx'

# Write DataFrames to separate sheets in the Excel file
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    sales.to_excel(writer, sheet_name='Sales Data', index=False)
    cust.to_excel(writer, sheet_name='Customer Details', index=False)
    prod.to_excel(writer, sheet_name='Product Summaries', index=False)