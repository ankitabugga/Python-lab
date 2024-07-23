import numpy as np

# Given temperature readings
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4, 25, 12, -4, -12])

# Identifying hot days (temperature > 35 degrees Celsius)
hot_days_indices = np.where(temperatures > 35)[0]

# Identifying cold days (temperature < 5 degrees Celsius)
cold_days_indices = np.where(temperatures < 5)[0]

# Creating formatted strings for hot days
hot_days_output = "Hot Days:\n\nDay\nTemperature (°C)\n"
for index in hot_days_indices:
    hot_days_output += f"{index + 1}\t{temperatures[index]}\n"

# Creating formatted strings for cold days
cold_days_output = "\nCold Days:\n\nDay\nTemperature (°C)\n"
for index in cold_days_indices:
    cold_days_output += f"{index + 1}\t{temperatures[index]}\n"

print(hot_days_output)
print(cold_days_output)




"""output
Hot Days:

Day
Temperature (°C)
3	36.8
6	38.7
10	37.2


Cold Days:

Day
Temperature (°C)
11	4.0
14	-4.0
15	-12.0


"""
