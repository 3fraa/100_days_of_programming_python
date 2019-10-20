#43
print("-------------Day 43-------------")
#Parent Class
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

x = person("Afraa", "Murad")
x.printname()
print()

#Child Class
class student(person):
    pass
y = student("Laila", "Haitham")
y.printname()
print()

class stu(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)
z = stu("Noha", "Mohammad")
z.printname()
print()


#44
#super() function
print("-------------Day 44-------------")
class stu1(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
j = stu1("Yasser", "AlTobati")
j.printname()
print()

#Add new Properties for Child Class
class stu2(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.gradutionyear = 2019
i = stu2("Reem", "Adel")
i.printname()
print(i.firstname, i.lastname, "graduate at " , i.gradutionyear)
print()

class stu3(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.gradutionyear = year
k = stu3("Dado", "AlTobati", 2019)
k.printname()
print(k.gradutionyear)
print()

#Add new methods for Child Class
class stu4(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradutionyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.gradutionyear)
r = stu4("Amal", "Khaled", 2019)
r.welcome()

