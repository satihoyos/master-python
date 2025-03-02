import math

a = 1
b= -5
c = 6
disc = b*b - 4*a*c
sol1 = (-b + math.sqrt(disc)) / (2*a)
sol2 = (-b - math.sqrt(disc)) / (2*a)

print("x={0}".format(sol1))
print("x={0}".format(sol2))
