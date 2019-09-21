Tuple = ('Afraa', 25, "Computer engineer", 3.75)

print ("is 3.75 in Tuple? " , 3.75 in Tuple)

if "Computer engineer" in Tuple:
    print("Afraa is Computer engineer")

#####################################################
print()

Tuple1 = ("python",)*3
print(Tuple1)
    
Tuple1 = ("python ")*3 #without comma
print(Tuple1) 

#####################################################
print()

T1 = (1, 3, 5, 7, 9)
T2 = (2, 4, 6, 8, 0)
T = T1 + T2
print(T)

T1 = ('a', 'b')
T2 = ('c', 'd')
T = T1 + T2
print(T)

T1 = ("Afraa", "Bassmah")
T2 = (1, "Dalal")
T = T1 + T2
print(T)

x = (3, 4, 5, 6)
x = x + (1, 2, 3)
print(x)

#####################################################
print()

print("The number of items in the x = " , len(x))
print("The number of items in the T = " , len(T))


#####################################################
print()

print( tuple((13, 14,15))) #use tuple() to creat a tuple

TT = tuple((13, 14,15)) 
print(TT)

list1 = [1,1,2,3,3,3,"A"]
TTT = tuple((list1))
print(TTT)

#####################################################
print()

print(TTT.count(1))
print(TTT.count(2))
print(TTT.count(3))
print(TTT.count("A"))

#####################################################
print()

print(TTT.index("A"))
print(TTT.index(3))


