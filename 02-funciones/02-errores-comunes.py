import math


def paradoja(a):
    b = math.sqrt(a)
    print(b)
    return a == b * b


def fibonacci(n):  # problema punto flotante
    phi = (1 + math.sqrt(5)) / 2
    return (phi ** n - (1 - phi) ** n) / math.sqrt(5)


def fibonacci2(n):  # problema punto flotante
    phi = (1 + math.sqrt(5)) / 2
    return int(round((phi ** n - (1 - phi) ** n) / math.sqrt(5)))


print(paradoja(2))
print(math.cos(math.pi/3) == 0.5)
print(fibonacci(4))
print(fibonacci2(4))





