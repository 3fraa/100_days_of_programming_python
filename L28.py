i = 10
while i > 0 :
    print(i)
    i -= 1

print()

x = 1
while x < 6 :
    print(x)
    if x == 3:
        break
    x += 1

print()

i = 0
while i < 6 :
    i += 1
    if i == 3 :
        continue
    print(i)
else :
    print("i is no longer less than six")
