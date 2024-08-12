#Write a Pandas program to create a Pivot table and find the item wise unit sold.
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('C:\\Users\\Acer\\Downloads\\salesdata.csv')

# Create a Pivot table to find item-wise units sold
pivot_table = pd.pivot_table(df, values='Units', index='Item', aggfunc='sum')

# Display the Pivot table
print(pivot_table)


#output
"""
              Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
"""
