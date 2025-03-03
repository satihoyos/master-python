a = True
b = False

print((a and b, a or b, a or True, b and False))

a, b = 2, 4
print(b == a * 2)
print((34 != 34, not (34 == 34), a * 3 >= 7, b * 2 < 8, b * 2 <= 8, a >= 2 or b < 7))
print((2 <= a and a < 7, a <= a < 7))

print("circle")
def is_in_circle(x, y, r):
    return x**2 + y**2 <= r


print((is_in_circle(0.5,0.5, 1), is_in_circle(0.5, 0.9, 1)))

def is_in_circle2(x, y, r):
    return "Dentro" if x**2 + y**2 <= r else "Fuera"


print((is_in_circle2(0.5,0.5, 1), is_in_circle2(0.5, 0.9, 1)))