def myFun(Family):
    for x in Family:
        print(x)
LailaFamily = list(("Laila", "Turki", "Yaser"))
myFun(LailaFamily)

print()

def myFun(Family):
        print(Family)
LailaFamily = list(("Laila", "Turki", "Yaser"))
myFun(LailaFamily)

print()

def myFun(x):
    return x-1  
print(myFun(4))
print(myFun(5))

print()

"""
def myFun(Family):
    for x in Family:
        return x + " is cute"
LailaFamily = list(("Laila", "Turki", "Yaser"))
print(myFun(LailaFamily))

print()
"""

def myF(A, B, c):
    print("The largest number is ", A)
myF(B=9, c=8, A=10)
myF(4,3,2) #without keyword

print()

def myFun(*Kids):
    print("The youngest child is " + Kids[1])
myFun("Reem", "Yasser", "Sanaa")

print()

def myFun(*Kids):
    print("The youngest child is" , Kids[1])
myFun("Reem", "Yasser", "Sanaa")

print()

#Recursion

def myFun_rec(x):
    if(x>0):  
        result = x + myFun_rec(x-1)
        #print(result)
    else:
        result = 0
    return result

print("Recursion Example Results")
print(myFun_rec(4)) # 4+myFun_rec(3) #3+myFun_rec(2) # 2+myFun_rec(1) #1+myFun_rec(0) # will print 10
print("\nRecursion Example Results")
print(myFun_rec(5))
print("\nRecursion Example Results")
print(myFun_rec(6))
print("\nRecursion Example Results")
print(myFun_rec(10))
print("\nRecursion Example Results")
print(myFun_rec(0))
print("\nRecursion Example Results")
print(myFun_rec(-4))

print()

def fact(num):
    if num == 0: return 1
    else: return num * fact(num-1)
print(fact(4))

print()

x = [1, 2, 3, 4, 5]
def add(array):
    if len(array)== 0 : return 0
    else: return array[0] + add(array[1:])
print(add(x)) # 1+array[2,3,4,5]    #1+14=15
              # 2+array[3,4,5]      #2+12=14
              # 3+array[4,5]        #3+9=12
              # 4+array[5]          #4+5=9
              # 5+array[]           #5

