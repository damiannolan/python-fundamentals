

def newtonsqrt(x):
    z = x / 2.0
    while True:
        z_next = (z + x / z) / 2.0
        if abs(z - z_next) < 0.00001:
            return z_next
        z = z_next

print(newtonsqrt(25))
