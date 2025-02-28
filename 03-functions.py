import math


def formar_numero(dec, uni):
    valor_decenas = 10 * dec
    valor_unidades = uni
    return valor_decenas + valor_unidades


def media(x, y):
    return (x + y) / 2


def media_4(a1, a2, a3, a4):
    suma = a1 + a2 + a3 + a4
    return suma / 4


def area_circulo(radius):
    return math.pi * radius ** 2


print((formar_numero(3,4), formar_numero(9, 2), formar_numero(0, 5)))
print((media(3, 25), media(3.4, 5.6), media(-1, -3)))
print(media_4(1.5, 9.1, 3.0, 6.7))
print("pi", math.pi)
print("area:", area_circulo(2))

# comentarios multiples lineas
"""
Esto 
    es 
        un 
            comentario
                multilinea
"""

def explicacio_metodo():
    """
    este es un ejemplo de la documentacion, de un metodo
    :return:
    """
    return "test"


print(explicacio_metodo.__doc__)


def lado_cuadrado (area):
    assert area >= 0, "El are debe ser positiva"
    return math.sqrt(area)


print(lado_cuadrado(2))
# print(lado_cuadrado(-2))


def ec_2_grado(a, b, c):
    """
    Precondition
    ------------
    a != 0 and b*b - 4*a*c >= 0

    Parameters
    ----------
    a, b, c : float
        coeficientes de la ecuacion

    Returns
    -------
    (float, float)
        Solutions of equations

    """
    disc = b*b - 4*a*c
    sol1 = (-b + math.sqrt(disc)) / (2*a)
    sol2 = (-b - math.sqrt(disc)) / (2*a)
    return sol1, sol2

a, b = ec_2_grado(1, -5, 6)
print((a, b))


def raiz(x, indice=2):
    return x ** (1/indice)


print("raiz:", (raiz(81), raiz(81, indice=2), raiz(81, indice=4), raiz(2, 3)))
