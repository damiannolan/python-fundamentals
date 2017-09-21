# Problem 10 - Reverse a String
# Use the extended slices syntax
# [begin:end:step]
# By leaving begin and end empty and stepping in the direction of -1
# We reverse the string

def reverseString(word):
    return word[::-1]

print(reverseString("reversed"))
