# Function to count the number of words in a string
def count_words(input_string):
    # Split the string by spaces and store it in a list
    words = input_string.split()
    
    # The number of words is the length of the list
    return len(words)

# Main function to get input and display the result
def main():
    # Get input from the user
    input_string = input("Enter a string: ")
    
    # Count the number of words in the string
    word_count = count_words(input_string)
    
    # Output the result
    print(f"The string contains {word_count} words")

# Call the main function
if __name__ == "__main__":
    main()
