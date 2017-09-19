def palindrome(word):
    # Extended Slices syntax [begin:end:step]
    # by leaving begin and end empty and stepping in a direction of -1
    # the string is reversed
    return word == word[::-1]

print(palindrome("lol"))

