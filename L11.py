#######################
"""Logical Operators"""

x = y = 3
z = 7
print("[x>y and z!=y] is ", x>y and z!=y) #F
print("[x>=y and z>y] is ", x>=y and z>y) #T
print("[x>y or x==z] is ", x>y or x==z)#F
print("[x>y or z>y] is ", x>y or z>y)#T
print(not x==y) #F

if not( x>z and x==y ):
    print ("x equal to y and x less than z")
else :
    print("There is error")

if x>z or x==y :
    print ("x equal to y or x less than z")
else :
    print("There is error")
print()
print()

########################
"""Identity Operators"""

a = [ 1,3 ]
b = [ 1,3 ]
c=a
print(a is b) #F
print(a is c) #T

d = ["Afraa" , "Noha"]
e = ["Afraa" , "Noha"]
f = d
print(d is e) #F
print(e is f) #F
print(f is d) #T
print(d == e) #T
print(e == f) #T
print(f == d) #T
print()
print()

##########################
"""Membership Operators"""


txt = "I have a beautiful friend"
print("friend" in txt)
print("end" in txt)
print("ing" in txt)
print("ing" not in txt)

myList = [1,2,22,100]
print(10 not in myList)
print(22 in myList)
print()
print()

#######################
"""Bitwise Operators"""

y = 9
z = 15
i = 27

y &= 3
z |= 3
i ^= 3 

print(y) #y= 1
print(z) #z= 15
print(i) #i= 24

