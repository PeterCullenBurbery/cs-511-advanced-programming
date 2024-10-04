# asterisk-bar-chart-positional-arguments.py

import sys
import ast  # To parse list-like string input

def draw_bar_chart(values):
    max_value = max(values)
    for value in values:
        bar_length = int((value / max_value) * 40)  # Proportionally scale to 40 asterisks
        print('*' * bar_length)

if __name__ == "__main__":
    # Ensure the user provided a list in the form [value1, value2, value3, etc...]
    if len(sys.argv) < 2:
        print("Please provide a list of values in the form [value1, value2, value3, etc...].")
        sys.exit(1)

    # Get the list input from command-line argument and convert it to a list
    try:
        values = ast.literal_eval(sys.argv[1])
        if not isinstance(values, list):
            raise ValueError
    except (ValueError, SyntaxError):
        print("Error: Please provide a valid list in the form [value1, value2, value3, etc...]")
        sys.exit(1)

    # Draw the bar chart with the provided values
    draw_bar_chart(values)
