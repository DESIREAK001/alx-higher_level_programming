#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert the lowercase letter to uppercase using ASCII manipulation
            uppercase_char = chr(ord(char) - 32)
            print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(char), end="")

    # Print a new line after processing the entire string
    print()

# Test the function
uppercase("Hello, World!")  # Output: HELLO, WORLD!
