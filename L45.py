#45
print("-------------Day 45-------------")
Tuple = ("Red", "Black", "Yellow")
myiter = iter(Tuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print()

for x in Tuple:
    print(x)
print()

name = "Afraa"
myiter = iter(name)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print()

for x in name:
    print(x)
print()

"""
Tuple = ("Red", "Black", "Yellow")
print(next(iter(Tuple)))
print(next(iter(Tuple)))
print(next(iter(Tuple)))
print()

name = "Afraa"
print(next(iter(name)))
print(next(iter(name)))
print(next(iter(name)))
print(next(iter(name)))
print(next(iter(name)))
print()
"""

#ترجع أرقام تبدأ من واحد، وكل مرة تزيد بواحد
class MyNum:
    def __iter__(self):
        self.firstNum = 1
        return self
    def __next__(self):
        x = self.firstNum
        self.firstNum += 1
        return x
myclass = MyNum()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print()

#StopIteration
class MyNum:
    def __iter__(self):
        self.firstNum = 1
        return self
    def __next__(self):
        if self.firstNum <= 20:
            x = self.firstNum
            self.firstNum += 1
            return x
        else:
            raise StopIteration
myclass = MyNum()
myiter = iter(myclass)

for x in myiter:
    print(x)
print()
