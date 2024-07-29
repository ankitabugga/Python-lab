import matplotlib.pyplot as plt

x = [0, 5, 9, 10, 15, 20, 25] 

y = [0, 1, 2, 3, 4, 5, 6]
# Create a line plot
plt.plot(x, y)
# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
# Show the plot
plt.show()
