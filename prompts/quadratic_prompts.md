# 1.To create a data table
Create a date table that has the dates from 03-01-2025 (March 1st, 2025)
to 05-31-2025 (May 31st, 2025)

# 2. Data cleaning and summarizing required data in one table
(fact_summary)
Create a Python code that:

1. Load data from:
 - fact_order_line table
 - dim_products sheet (skip first row, use second row as headers)
 - dim_customers sheet (skip first row, use second row as headers)
 - Exchange Rate sheet (skip first row, use second row as headers)

2. Cleans the data:
 - Convert product_id and customer_id to numeric
 - Strip whitespace from IDs
 - Remove rows with NULL IDs
 - vert IDs to integers
 - Convert dates to datetime

3. Merges the tables:
 - Orders with products using product_id
 - Result with customers using customer_id
 - Result with exchange rates using order_placement_date

4. Calculates total amounts:
 - For USD currency: price_USD * USD_INR_Rate * order_qty
 - For INR currency: price_INR * order_qty

5. Clean final output:
 - Drop intermediate columns: price_USD, price_INR, currency, Date, USD_INR_Rate
 - Keep only essential columns: order details, IDs, dates, quantities, delivery information,
and total_amount (in INR)
dont use exchange rate for anything . if required make it 1 usd = 90 inr

# 3. KPIs
1. Total Order Lines

2. Line Fill Rate

3. Volume Fill Rate

4. Total Orders

5. On Time Delivery %

6. In Full Delivery %
7. On Time In Full %
