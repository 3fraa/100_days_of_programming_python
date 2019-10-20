#48
print("-------------Day 48-------------")
#Local Scope
def myfunct():
    x = 10
    print(x)
myfunct() #10

#print(x) #will give us error cuz "x" is not available outside the function

def myfunct():
    x = 10
    def myinnerfunct():
        print(x)
    myinnerfunct()
myfunct() #10
print()

#Global Scope
x = 10
def myfunct():
    print(x)
myfunct()#10
print(x) #10
print()

#49
print("-------------Day 49-------------")
x = 200
def myfunct():
    x = 10
    print(x)
myfunct() #10
print(x) #200
print()

def myfunct():
    global x
    x = 10
    print(x)
myfunct() #10 #here is an important call the function
print(x) #10
print()

z = 400
def myfunct():
    global z
    z = 450
    print(z)
myfunct()#450
print(z) #450
print()

z = 400
def myfunct():
    z = 450
    print(z)
myfunct()#450
print(z) #400
print()
