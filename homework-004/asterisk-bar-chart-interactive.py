# asterisk-bar-chart-interactive.py

import ast  # To parse list-like string input

def draw_bar_chart(values):
    max_value = max(values)
    for value in values:
        bar_length = int((value / max_value) * 40)  # Proportionally scale to 40 asterisks
        print('*' * bar_length)

if __name__ == "__main__":
    # Prompt the user to enter a list of values
    input_string = input("Enter a list of values in the form [value1, value2, value3, etc...]: ")

    # Convert the input string to an actual list
    try:
        values = ast.literal_eval(input_string)
        if not isinstance(values, list):
            raise ValueError
    except (ValueError, SyntaxError):
        print("Error: Please provide a valid list in the form [value1, value2, value3, etc...]")
        exit(1)

    # Draw the bar chart with the provided values
    draw_bar_chart(values)
