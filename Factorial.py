def factorial(y):
    x = y

    count = 1
    z = 1

    while z <= x:
        count = count * z
        z = z + 1
        print(count)

factorial(6)