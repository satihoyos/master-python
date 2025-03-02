def factores(num):
    divisores = (2, 3, 5, 6, 7, 11)

    i = 0
    while i < len(divisores):
        divisor = divisores[i]

        if divisor > num:
            break

        if num % divisor != 0:
            i = i + 1
            continue

        print("{0}|{1}".format(num, divisor))
        num = num // divisor

    print("{0}|".format(num))


factores(190)
