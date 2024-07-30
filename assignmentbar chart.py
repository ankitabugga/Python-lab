import matplotlib.pyplot as plt

# Categories and expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.bar(categories, expenses, color='skyblue')

# Add titles and labels
plt.title('Monthly Expenses by Category')
plt.xlabel('Categories')
plt.ylabel('Expenses ($)')
#plt.grid(axis='y')

# Show the plot
plt.show()
