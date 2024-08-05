import pandas as pd

# Expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data (example data in USD)
expenses = [500, 200, 1200, 300, 150]

# Create a Pandas Series
expenses_series = pd.Series(data=expenses, index=categories)
print(expenses_series )



#output:
"""Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
dtype: int64
"""
