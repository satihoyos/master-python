# funcion factorial
def factorial(n):
    acum = 1
    for i in range(1, n + 1):
        acum = acum * i
    return acum


print(factorial(5))
print(factorial(500))

# calling factorial with different values
for k in range(1, 5+1):
    print(k, "->", factorial(k))

print("-------------------------")

for k in [1, 10, 20, 30]:
    print(k, "->", factorial(k))


