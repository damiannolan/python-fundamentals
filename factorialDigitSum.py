# Problem 4 -  Find the factorial of a number n - eg: 5! = 5 * 4 * 3 * 2 * 1
# Then add up the singles digits of the outcome

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# Call the fact function passing 100 as the argument
factNum = fact(100)

# By using str(factNum) we iterate over the each digit in the large number and sum() them
# while parsing back to an integer int(i)
print(sum([int(i) for i in str(factNum)]))
