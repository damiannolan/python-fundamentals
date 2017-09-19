import random

tries = 0
n = random.randint(1, 20)
print("Guess a number between 1 and 20!")

while 1: 
    tries += 1
    guess = int(input())

    if guess < n:
        print("Too low!")
    elif guess > n:
        print("Too high")
    else:
        print("Congrats, you guessed it in %d tries!" % tries)
        break

