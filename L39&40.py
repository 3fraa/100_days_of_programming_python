#Sol of Q1:
print("Sol of Q1:")
#1
def Fun(num1, num2):
    if num2 > 0 : return num1 * Fun(num1,num2-1)
    else : return 1
print(Fun(5, 3))
print()

#2
def Fun(num):
    if num == 3 : return 3
    else : return num ** Fun(num-2)
print(Fun(5))
print()

#Sol of Q2:
print("Sol of Q2:")
List = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
#1
x = list(filter(lambda x: (x >= 0), List))
print(*x)
print()

#2
y = filter(lambda x: x > 0,List)
print(*y)
print()

#3
pos_num =[]
ispos = lambda x: x > 0
for y in List:
    if (ispos(y)):
        pos_num.append(y)
print(pos_num)
print()

#4
x = lambda y: y if y > 0 else None
for i in List:
    if x(i) != None:
        print(x(i))
print()
