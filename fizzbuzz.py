# Problem 3 - FizzBuzz
# Use modulus operator to achieve printing either - Fizz, Buzz or FizzBuzz
# Otherwise print the number

for i in range(100):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
