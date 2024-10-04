def main():
    numbers = []  # List to store all the numbers entered by the user

    while True:
        user_input = input("Please enter a number (or type 'exit', 'quit', 'stop', 'calculate' to finish): ").strip()

        # Check if the user wants to stop entering numbers
        if user_input.lower() in ['exit', 'quit', 'stop', 'calculate']:
            break

        # Try to convert the input to an integer
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    # Once user decides to stop, calculate and display the results
    if numbers:  # Check if the user entered any numbers
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
    else:
        print("No numbers were entered.")

# Run the program
if __name__ == "__main__":
    main()
