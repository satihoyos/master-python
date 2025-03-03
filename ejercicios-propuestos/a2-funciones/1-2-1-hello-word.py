def hello_word(name):
    """
    function that prints in the prompt 'hola'+name

    :param name: string
    :return: void
    """
    print("Hola, {0}".format(name))


name = input("como te llamas?")
hello_word(name)
