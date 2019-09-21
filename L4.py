import random

#different type
x = 1
y = 1.82
z = 1J

x1 = type(x)

print(x1)
print(type(y))
print(type(z))
print()

#integer
a = 154367281098932786754617
b = -24124

print(type(a))
print(type(b))
print()

#float
c = -24124.23
d = 4e3
e = 23E5

print(type(c))
print(type(d))
print(type(e))
print()

#complex
f = 3+2J
g = -5J

print(type(f))
print(type(g))
print()

#Type Conversion
h = float(x)
i = int(y)
j = complex(x)
k = complex(y)
print(h)
print(i)
print(j)
print(k)
print()
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print()

#print random number
print(random.randrange(4,20))
      








