def islower(c):
    # Check if the ASCII value of the character is within the range of lowercase letters
    return 97 <= ord(c) <= 122

# Test the function
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('1'))  # False