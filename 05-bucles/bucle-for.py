n = 10
suma = 0
for i in range(1, n + 1):
    suma = suma + i

print("suma: ", suma)


def sum_acot(n: int) -> int:
    suma2 = 0
    for i in range(1, n + 1):
        suma2 = suma2 + i
    return suma2


print("suma2:", sum_acot(10))


def nota_media(lista_notas):
    suma = 0.0
    for nota in lista_notas:
        suma = suma + nota
    return suma / len(lista_notas)


print("media notas:", nota_media([4.5, 6, 5]))

print("range:", list(range(10)))
print("range:", (list(range(5, 10)), list(range(5, 20, 3)), list(range(10, 5, -1))))

###################
import random


def lista_aleatoria(n):
    lista = []
    for x in range(n):
        lista.append(random.randint(0, 100))
    return lista


print("lista aleatoria: ", lista_aleatoria(3))


def romano_a_entero(romano):
    valor = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    romano_init = romano[-1]
    print("romano_init", romano_init)
    total = valor[romano_init]
    for i in range(len(romano) - 1):
        cifra, siguiente = valor[romano[i]], valor[romano[i + 1]]
        total = total + (cifra if cifra >= siguiente else - cifra)
    return total


for r in ["I", "IV", "XXXIX", "XLV", "LXIV", "MCDXCII"]:
    print(r, romano_a_entero(r))

for c in 'hola':
    print(c, end=' ')

for c in 'Buenas Tardes Angel':
    print(c.lower(), ord(c.lower()), c.upper(), ord(c.upper()))

for _ in range(3):
    print("test")

