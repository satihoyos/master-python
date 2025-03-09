print("Strip: quita espacios y saltos de linea")
a = '   hola    ' + '\n'
print(a)
print(a.strip())

print("Split: retorna lista a partir de un caracter en blanco o el caracter indicado en un txt")
a = 'manderas de vivir'
print(a.split())

a = 'manderas.de.vivir'
print(a.split('.'))

lista = ['uno', 'dos', 'tres', 'cuatro']
print(''.join(lista))
print(' '.join(lista))
print('-=-'.join(lista))
