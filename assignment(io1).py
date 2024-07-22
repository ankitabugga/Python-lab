
filename = "d:\\demo\\sem4.txt"  # Specify the name of the file to open

try:
    # Attempt to open the file in read mode
    with open(filename, 'r') as file:
        # Read the contents of the file
        content = file.read()
        # Print the contents of the file
        print(content)
except FileNotFoundError:
    # Handle the case where the file does not exist
    print(f"The file '{filename}' does not exist.")



#output
    #nnnnnnnnnnnnnnn
'''helyyyyyloworld

mmmmmmmmmmmmmmmmmmqqqqqqqhelloworld

'''
