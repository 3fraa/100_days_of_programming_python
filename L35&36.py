#Lambda

x = lambda a : a * 10
y = lambda b : "Afraa " + b
z = lambda c, d, e : c + d + e
print("3 * 10 =", x(3))
print(y("mhm"))
print("16 + 11 + 3 =", z(16, 11, 3))

print()

def fun(n):
    return lambda a : a * n
x = fun(3)
print(x(2))
y = fun(4)
print(y(2))
z = fun(5)
print(z(3))

print()
def fun(n):
    return lambda a : a * n
x = fun(3)
print(x(2))
print()


g = lambda x: "Afraa {}".format(x)
print(g("Murad"))

g = lambda x: f'Afraa {x}'
print(g('Murad'))

g = lambda x: "Afraa " + x
print(g("Murad"))
