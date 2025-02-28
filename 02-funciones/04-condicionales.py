def aprobados(nota):
    if nota >= 5.0:
        return True
    else:
        return False


print((aprobados(3.0), aprobados(7.5), aprobados(5.0)))


def aprobados2(nota: float) -> bool:
    # If you want to put docstring of method, skip types' arguments and return
    if nota >= 5.0:
        return True
    else:
        return False


print((aprobados(3.0), aprobados(7.5), aprobados(5.0)))


def aprobados3(nota):
    return True if nota >= 5.0 else False # Expresion condicional


print((aprobados(3.0), aprobados(7.5), aprobados(5.0)))


def aprobados4(nota):
    return nota >= 5.0


print((aprobados(3.0), aprobados(7.5), aprobados(5.0)))


def valor_absoluto(x):
    if x < 0:
        x = -x
    return x


print(valor_absoluto(-10), valor_absoluto(10))


def max_min(x, y):
    return max(x, y), min(x, y)


print(max_min(2, 3))


def calificacion(num_nota):
    if num_nota < 5:
        return "Suspenso"
    elif num_nota < 7:
        return "Aprobado"
    elif num_nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"


print(calificacion(8))
