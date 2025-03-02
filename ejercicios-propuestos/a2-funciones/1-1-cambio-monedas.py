
def calculate_division(dividendo, divisor):
    """
     Funcion que realiza la division entre dos enteros
        division / divisor

     Precondition
     ------------
     divisor != 0

    :param dividendo: int
    :param divisor: int

    :return: (cociente, resto)
    """
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto


def calculate_change(dinero, monedas_diccinario, position_key):
    """
    function that calculates how many coins have an amount of money,
    the money dictionary's key contains the value of coin that it needs to be
    calculated at the end the amount of each key will be safe in the value

    Precondition
    ------------
    money_diccionario'key == number as string

    :param dinero: int
    :param monedas_diccinario:  dictionary the key should be string number, value of coin,
    :param position_key:
    :return: void
    """
    key = list(monedas_diccinario)[position_key]
    monedas_diccinario[key], resto = calculate_division(dinero, int(key))
    if resto > 0:
        calculate_change(resto, monedas_diccinario, position_key + 1)


def cambio(dinero):
    """
    function that calculates amount of coins in 25, 5 and 1 units

    Precondition
    ------------
    dinero > -1

    :param dinero: int
    :return: str with money values
    """
    if dinero < 0:
        raise ValueError("Dinero should be a positive number")

    cambio_monedas = {'25': 0, '5': 0, '1': 0}
    calculate_change(dinero, cambio_monedas, 0)
    keys = list(cambio_monedas)
    response = ""
    for i in keys:
        msg = "Monedas de {0}: {1}, ".format(i, str(cambio_monedas[i]))
        response = response + ' ' + msg
    return response


print(cambio(459))
print(cambio(20))
print(cambio(4))
print(cambio(100))
