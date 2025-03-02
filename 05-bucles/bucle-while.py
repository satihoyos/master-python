n = 10
suma = 0
i = 1
while i <= n:
    suma = suma + i
    i = i + 1

print(suma)


def suma_hasta(n):
    suma = 0
    i = 1
    while i <= n:
        suma = suma + i
        i = i + 1

    return suma


print((suma_hasta(7), suma_hasta(-3)))


def suma_de_cifras(n):
    suma = 0
    while n != 0:
        suma = suma + n % 10
        n = n // 10
    return suma


def divisible_by_3(n):
    copy = n
    while copy > 9:
        copy = suma_de_cifras(copy)
        print("Copy: ", copy)
    return (copy == 0) or (copy == 3) or (copy == 6) or (copy == 9)


print(divisible_by_3(3341224134132411231))


def sum_par_impar(n):
    pos_par = True
    pares = 0
    impares = 0

    while n != 0:
        digit = n % 10
        if pos_par:
            pares = pares + digit
        else:
            impares = impares + digit
        n = n // 10
        pos_par = not pos_par
    return (pares, impares)


def divisible_11(n):
    while n > 11:
        pares, impares = sum_par_impar(n)
        if pares > impares:
            n = pares - impares
        else:
            n = impares - pares
    return n == 0 or n == 11


print("Divisible 11", divisible_11(11))
print("Divisible 11", divisible_11(135777972))



