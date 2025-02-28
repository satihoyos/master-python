# Enteros

print((3+7, 3-7, 3 + 2*7, (3+2)*7, 1 + 2 * 3**2))

#  / -> division No real
#  // -> division No entero

print((17 / 5, 17 // 5, 17 % 5))

########
print((37 / 5, 37 // 5, 37 % 5))
print((-37 / 5, -37 // 5, -37 % 5))
print((37 / -5, 37 // -5, 37 % -5))
print((-37 / -5, -37 // -5, -37 % -5))  # negative module
##############
# With variables
dividendo = 17
divisor = 5
cociente = dividendo // divisor
resto = dividendo % divisor

print((dividendo, divisor * cociente + resto))
x = (4*9)/6
y = (4*9)//6
print((type(x), type(y), type(x + y)))

def poli (x):
    c0 = -6
    c1 = -4 * x
    c2 = 3 * x**2
    return c0 + c1 + c2


print(poli(5))


def poli2(x):
    s = 0
    pot = 1
    s = s + (-6 * pot)
    pot = x * pot
    s = s + (-4 * pot)
    pot = x * pot
    return s + (3 * pot)


print(poli2(5))


def poli3(x):
    s = 0
    pot = 1
    for coef in [-6, -4, 3]:
        s = s + (coef * pot)
        pot = x * pot
    return s


print(poli3(5))


def poli4(x, coeficientes):
    s = 0
    pot = 1
    for coef in coeficientes:
        s = s + (coef * pot)
        pot = x * pot
    return s

print(poli4(5,[-6, -4, 3] ))


# punto flotante
a = 2.0
b = 3.0

suma, resta, multi, divi = a + b, a -b, a * b, a / b
print((suma, resta, multi, divi))
print(a * 7)


def poli5 (x):
    return -6.0 + -4.0 * x + 3 * x ** 2


print(poli5(5))



# numeros complejos


