print("Empieza el juego")
input("Para este truco vas a necesitar un dado si no lo tienes inventate los resultado ...")
input("Lanza el dado y fijate en el resultado (supongamos que obtienes un 4)")
input("Multiplica por 2 y suma 5 al resultado ...")
input("tenemos 4 x 2 = 8; 8 + 5 = 13, multiplica lo que tienes ahora por 5... 13 x 5 = 65")
input("Y ahora, lanza el dado de nuevo... Supongamos que obtienes un 3. Anade la puntuacion obtenida al resultado anterior")
resultado_obtenido = input("Ahora dime el resultado obtenido: ")
print("Ahora adivinare el numero de los dados dejame pensar...")

resultado = int(resultado_obtenido) - 25
num_1 = resultado // 10
num_2 = resultado % 10
input("Los numeros de los dados fueron {0}, {1} \nHasta la otra.".format(num_1, num_2))

