def hello_word(name, edad):
    print("Hola, {0}, pronto cumpliras {1}".format(name, int(edad) + 1))


name = input("Dime tu nombre:")
edad = input("Dime tu edad:")
hello_word(name, edad)
