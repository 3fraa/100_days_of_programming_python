##########################
"""Arithmetic operators"""
a = 9
b = 3

print(a + b) #12
print(a - b) #6
print(a * b) #27
print(a / b) #3.0
print(a % b) #0     #باقي القسمة
print(a ** b) #729  #اس 
print(a // b) #3    # القسمة بدون مابعد الفاصلة
print()
print()


##########################
"""Assignment operators"""
a += 2 
b -= 2 
print(a) #a=11
print(b) #b=1

c = "Afraa"
c += " "
c += "Murad"
print(c) #Afraa Murad

a *= 2 
b /= 2 
print(a) #a=22
print(b) #b=0.5

a %= 2 
b //= 2 
print(a) #a=0
print(b) #b=0.0

x = 12
y = 9
z = 15
i = 27
j = 17
k = 7

x **= 3
y &= 3
z |= 3
i ^= 3 
j >>= 3
k <<= 3
print(x) #x=1728
print(y) #y= 1
print(z) #z= 15
print(i) #i= 24
print(j) #j=
print(k) #k=
print()
print()

##########################
"""Comparison operators"""
num1 = num2 = 10
num3 = 15.2
num4 = 14

num = "num1={} , num2={} , num3={} , num4={}"
print(num.format(num1,num2,num3,num4))

print(num1 == num2) #T
print(num1 == num3) #F
print(num1 != num3) #T
print(num1 != num2) #F
print(num3 >= num2) #T
print(num4 >= num3) #F
print(num1 <= num2) #T
print(num3 <= num1) #F
print(num3 > num2) #T
print(num4 > num3) #F
print(num1 < num3) #T
print(num1 < num2) #F
