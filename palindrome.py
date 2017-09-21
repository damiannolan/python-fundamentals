# Problem 7 - Palindrome Test
# Create a function that takes a word as the arguement
# Use the extended slices syntax
# The function will return either true or false depending on the input

def palindrome(word):
    # Extended Slices syntax [begin:end:step]
    # by leaving begin and end empty and stepping in a direction of -1
    # the string is reversed
    return word == word[::-1]

print(palindrome("lol"))

