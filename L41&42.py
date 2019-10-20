#41
print("-------------Day 41-------------")
class car:
    color = "black"
print(car)
print()

class car:
    color = "black"
BMW = car()   #object BMW
print(BMW.color)
print()

class Human:
    def __init__(self, name, age): # للاشارة أن الدالة تابعة للكلاس self
        self.name = name
        self.age = age   
x = Human("Jomanh", 25)
print(x.name)
print(x.age)
print()

class Human:
    def __init__(variable, name, age):
        variable.name = name
        variable.age = age
    def myfunc(sen):
        print("Hello, my name is " + sen.name)  
x = Human("Jomanh", 25)
x.myfunc()
print()

#42
print("-------------Day 42-------------")
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello, my name is " + self.name + " and I have " + self.age + " years old")  
x = person("Jomanh", "25")
x.myfunc()
x.name = "Laila"
x.age = "24"
x.myfunc()
print(x.age)
print(x)
print()
"""
del x.age 
x.myfunc()
print()

del x
print(x)
"""
