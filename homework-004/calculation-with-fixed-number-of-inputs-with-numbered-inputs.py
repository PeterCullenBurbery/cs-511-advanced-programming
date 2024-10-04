def main():
    # Define the number of inputs required
    num_inputs = 10
    numbers = []  # List to store all the numbers entered by the user

    # Loop to get the fixed number of inputs from the user
    for i in range(1, num_inputs + 1):
        while True:
            user_input = input(f"Please enter a number: ").strip()

            # Try to convert the input to an integer
            try:
                number = int(user_input)
                numbers.append(number)
                break  # Break out of the while loop once a valid number is entered
            except ValueError:
                print("Invalid input. Please enter an integer value.")

    # (a) Calculate the sum
    total_sum = sum(numbers)

    # (b) Calculate the product
    product = 1
    for num in numbers:
        product *= num

    # (c) Find the highest number
    highest_number = max(numbers)

    # Display the results
    print("************************************************************")
    print("****Solution-Q2.**********************************************")
    print("************************************************************")
    print(f"Answer for Q2 (a): The sum of all the numbers is: {total_sum}")
    print(f"Answer for Q2 (b): The product of all the numbers is: {product}")
    print(f"Answer for Q2 (c): The largest number you entered was: {highest_number}")

# Run the program
if __name__ == "__main__":
    main()
