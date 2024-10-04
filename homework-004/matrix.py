# Function to create and populate a 3x3 matrix
def populate_matrix():
    matrix = []  # To store the 3x3 table
    
    # Loop to process each row
    for row in range(1, 4):  # We have 3 rows
        print(f"Processing row {row}")
        row_data = []  # To store values for the current row
        
        # Loop to get values for each column in the current row
        for col in range(1, 4):  # We have 3 columns
            value = input(f"Enter col {col} value: ")
            row_data.append(value)  # Add the input to the current row
        
        matrix.append(row_data)  # Add the completed row to the matrix
    
    # Display the matrix
    print("The elements in the table are:")
    print(matrix)

# Call the function
if __name__ == "__main__":
    populate_matrix()
