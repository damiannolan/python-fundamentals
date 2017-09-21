# Problem 6 - Largest and Smallest
# Simply use max() and min() to achieve the desired results

lst = []

num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("Maximum element in the list is : %d" % max(lst))
print("Minimum element in the list is : %d" % min(lst))
