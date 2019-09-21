a = b = 10
c = 3

if a > b :
    print("a is greater than b")
elif a < b :
    print("a is less than b")
else :
    print("a is equal to b")
if len("Afraa") == len("Laila"): print("Afraa ana Laila have the same number of characters")
print("a is equal to b") if a == b else print("a is not equal to b")
print("<") if a < b else print(">") if a > b else print("=")

print()

if a > c and b > c :
    print("c is the lowest number")
if a > c or b < c :
    print("mayb a greater than c or b less than c")

print()

if c < 20 :
    print("Less than twenty")
    if c < 10 :
        print("and less than ten")
        if c < 5 :
            print("and less than five")
        else : 
            print("but not less than five")
    else :
        print("but not less than ten")
else :
    print("Greater than twenty")

print()


