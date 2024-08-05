import pandas as pd

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Create a Pandas Series
series = pd.Series(students, exam_scores)

# Display the Series
print(series)



#output
"""
92      Alice
88        Bob
76    Charlie
94      David
82        Eve
90      Frank
85      Grace
89     Hannah
78        Ivy
91       Jack
dtype: object
"""
