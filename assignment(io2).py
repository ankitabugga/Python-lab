filename = "ABC.txt"  # Specify the name of the file to open

try:
    # Open the file in read mode
    with open("d:\\demo\\ABC.txt", 'r') as file:
        # Read the contents of the file
        content = file.read()
        # Split the content into words based on whitespace
        words = content.split()
        # Count the number of words
        word_count = len(words)
        # Display the total number of words
        print(f"Total number of words in the file '{filename}': {word_count}")
except FileNotFoundError:
    # Handle the case where the file does not exist
    print(f"The file '{filename}' does not exist.")
except Exception as e:
    # Handle other potential exceptions
    print(f"An error occurred: {e}")




#output
    #Total number of words in the file 'ABC.txt': 2
