# Using a lambda function

x = 20.0

z_next = lambda z: (z - ((z*z - x) / (2 * z)))

current = 1.0

while current != z_next(current):
    current = z_next(current)


# Regular function

x = 20

def z_next(z):
    return (z - ((z*z - x) / (2 * z)))

current = 1.0

while current != z_next(current):
    print("current guess: %0.10f\t Next guess: %0.10f" % (current, z_next(current)))
    current = z_next(current)
