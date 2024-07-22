import numpy as np

# Create an array with values ranging from 2 to 10
array = np.arange(2, 11)

# Reshape the array into a 3x3 matrix
matrix = array.reshape(3, 3)

print(matrix)


#output
'''[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]'''
