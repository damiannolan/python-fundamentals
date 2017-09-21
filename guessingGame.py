# Probelm 5 - Guessing Game
# Use random to get a random number between 1 and 20
# Create a while loop and recieve input guesses
# Append each try to a list of attempts - (useful later)
# When the correct answer is entered - break the loop
# Print the number of distinct tries using len() and set()

import random

tries = []
n = random.randint(1, 20)
print("Guess a number between 1 and 20!")

while 1: 
    guess = int(input())

    if guess < n:
        print("Too low! Try again >:)")
        tries.append(guess)
    elif guess > n:
        tries.append(guess)
        print("Too high! Try again >:)")
    else:
        tries.append(guess)
        print("Congrats, you guessed it in %d tries!" % len(set(tries)))
        break 
