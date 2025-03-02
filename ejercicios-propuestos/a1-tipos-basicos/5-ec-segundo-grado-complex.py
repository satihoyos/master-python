import cmath

a = 1
b = -1
c = 6
disc = b*b - 4*a*c
sol1 = (-b + cmath.sqrt(disc)) / (2*a)
sol2 = (-b - cmath.sqrt(disc)) / (2*a)

print("x={0}".format(sol1))
print("x={0}".format(sol2))
