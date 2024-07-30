import matplotlib.pyplot as plt

# Define the days and temperature data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create a line chart

plt.plot(days, temperature,marker='o',  color='r', linewidth=2, markersize=6)

# Add titles and labels
plt.title('Daily Temperature Changes Over the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')
plt.grid(True)

# Show the chart
plt.show()
