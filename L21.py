theSet = {"Afraa", "Laila", 3, 3.75, "Arwa", "Azzah", "Asma"}

print("The number of items in a theSet = " , len(theSet))

theSet.remove("Arwa")
print(theSet)
theSet.discard(3)
print(theSet)
print(theSet.pop())
print(theSet)
x = theSet.pop()
print("x = " ,x)
print(theSet)
print()

theSet = {"Afraa", "Laila", 3, 3.75, "Arwa", "Azzah", "Asma"}
theSet.clear()
print(theSet)
print()

"""
thisSet = {"Afraa", "Laila", 3, 3.75, 5}
del thisSet()
print(thisSet)
"""
newSet = set((2, 4.4, "Hi"))
print(newSet)

S = newSet.copy()
print("S = " ,S)

print()
########################################
print("###############################")
print()

print("Difference")
S1 = {"Afraa", "Laila", 3, 4, 5.6}
S2 = set(("Afraa", "Noha", 7, 3))

print("S1 diff S2: ", S1.difference(S2)) #Laila, 4, 3.6
print("S2 diff S1: ",S2.difference(S1)) #Noha, 7

print("S1-S2: ",S1-S2) 
print("S2-S1: ",S2-S1)

print("S1: " , S1)
print("S2: " , S2)

print()

S1 = {"Afraa", "Laila", 3, 4, 5.6}
S2 = set(("Afraa", "Noha", 7, 3))
S1.difference_update(S2) 
print("S1: " , S1)
print("S2: " , S2)

S1 = {"Afraa", "Laila", 3, 4, 5.6}
S2 = set(("Afraa", "Noha", 7, 3))
S2.difference_update(S1) 
print("S1: " , S1)
print("S2: " , S2)

print()
########################################
print("###############################")
print()

print("Intersection & Isdisjoint & issubset & issuperset")
S1 = {"Afraa", "Laila", 3, 4, 5.6}
S2 = set(("Afraa", "Noha", 7, 3))
S3 = {"Afraa", "Walaa"}
S4 = {"Arwa",}
S5 = {"Afraa",}
print("S1 intersection S2: ", S1.intersection(S2)) #Afraa, 3
print("S2 intersection S1: ",S2.intersection(S1,S3)) #Afraa
print("S1: " , S1)
print("S2: " , S2)
print("S1 and S2 are disjoint?", S1.isdisjoint(S2)) #F   
print("S1 and S4 are disjoint?", S1.isdisjoint(S4)) #T
print("S1 subset S2?", S1.issubset(S2)) #F
print("S5 subset S1?", S5.issubset(S1)) #T
print("S1 superset S2?", S1.issuperset(S2)) #F   
print("S2 superset S5?", S2.issuperset(S5)) #T

print()

S1 = {"Afraa", "Laila", 3, 4, 5.6}
S2 = set(("Afraa", "Noha", 7, 3))
S3 = {"Afraa", "Walaa"}

S1.intersection_update(S2)
S2.intersection_update(S1,S3)

print("S1: " , S1)
print("S2: " , S2)

print()
########################################
print("###############################")
print()

print("Union")
S1 = {"Afraa", "Laila", 3, 4, 5.6}
S2 = set(("Afraa", "Noha", 7, 3))
S3 = {"Afraa", "Walaa"}

print("S1 U S2 : ", S1.union(S2)) 
print("S1 U S2 U S3 :", S1.union(S2, S3))


print()
########################################
print("###############################")
print()

print("symmetric_difference & symmetric_difference_update")
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
print(A.symmetric_difference(C))
print(B.symmetric_difference(C))
#print(C.symmetric_difference(A)) #ERROR! 'dict' object has no attribute 'symmetric_difference'
#print(C.symmetric_difference(B)) #ERROR! 'dict' object has no attribute 'symmetric_difference'
print()
print(A)
print(B)
print(C)
print()

A.symmetric_difference_update(B)
print(A)
print(B)
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
B.symmetric_difference_update(A)
print(A)
print(B)
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
print()
