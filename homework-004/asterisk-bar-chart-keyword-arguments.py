# asterisk-bar-chart-keyword-arguments.py

import argparse
import ast  # To parse list-like string input

def draw_bar_chart(values):
    max_value = max(values)
    for value in values:
        bar_length = int((value / max_value) * 40)  # Proportionally scale to 40 asterisks
        print('*' * bar_length)

if __name__ == "__main__":
    # Setup argparse to handle keyword arguments
    parser = argparse.ArgumentParser(description='Draw a bar chart with asterisks based on values.')
    
    # Expecting a string input that looks like a list: [value1, value2, value3, etc...]
    parser.add_argument('-values', type=str, required=True, help='List of values in the form [value1, value2, value3, etc...]')

    # Parse the arguments
    args = parser.parse_args()

    # Convert the string argument to an actual list
    try:
        values = ast.literal_eval(args.values)
        if not isinstance(values, list):
            raise ValueError
    except (ValueError, SyntaxError):
        print("Error: Please provide a valid list in the form [value1, value2, value3, etc...]")
        exit(1)

    # Draw the bar chart with the provided values
    draw_bar_chart(values)
