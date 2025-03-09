import requests

url_quijote = "https://www.gutenberg.org/cache/epub/2000/pg2000.txt"
f = requests.get(url_quijote)

print(f.encoding)
texto = f.text.split('\n')
for line in texto[613:620]:
    print(line)

palabras = "Dijo Don Quijote: ¿Qué tal Sancho? Bien señor, pero rendido; y dolorido por los lances del día..."
print([palabra for palabra in palabras.split()])
print([palabra.strip(" ,;:.¡!¿?") for palabra in palabras.split()])

for line in texto[613:625]:
    palabras = line.strip().split()
    print(palabras)
    pal_limpias = [palabra.strip(" ,;:.¡!¿?") for palabra in palabras]
    print(pal_limpias)
    print()
