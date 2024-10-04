# Function to repeat the string and join with a delimiter
def repeat_string_riffle():
    # Step (a): Ask the user for the input string
    input_string = input("Enter a string: ")
    
    # Step (b): Ask for the number of repetitions
    repetitions = int(input("How many repetitions? "))
    
    # Step (c): Ask for the delimiter to separate the repetitions
    delimiter = input("Separated by? ")
    
    # Repeat the string and join with the delimiter
    result = (delimiter).join([input_string] * repetitions)
    
    # Output the result
    print(result)

# Call the function
if __name__ == "__main__":
    repeat_string_riffle()
