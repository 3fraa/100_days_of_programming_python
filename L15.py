list_int = [2, 4, 6, 8, 10, 12, 14 ]
list_str = ["Afraa", "Noha", "Leen", "Joudi"]
list_mix = [2.4 , 7 , 7]

print("number of item list_int = " ,len(list_int))

list_int.append(16)
print(list_int)

list_str.append("Laila")
print(list_str)

list_str.insert(2,"Walaa")
print(list_str)

print()
print("################################################")
print()

list_int.remove(4)
print(list_int)

list_mix.remove(7)
print(list_mix)

list_int.pop(1)
print(list_int)

list_str.pop()
print(list_str)

list_int.clear()
print(list_int)

print()
print("################################################")
print()

print("list_str  = " , list_str)
list_name = list_str.copy()
print("list_name = " , list_name)
list_name.remove("Walaa")
print("list_name = " , list_name)
print("list_str  = " , list_str)

print()

print("list_str   = " , list_str)
list_name1 = list_str
print("list_name1 = " , list_name1)
list_name1.remove("Walaa")
print("list_name1 = " , list_name)
print("list_str   = " , list_str)

print()

oldlist = ["rain" , "dust" , "wind"]
print("oldlist = " , oldlist)
newlist = list(oldlist)
print("newlist = " , newlist)
newlist.pop(0)
print("oldlist = " , oldlist)
print("newlist = " , newlist)

print()

courselist = list(("electronics", "embedded system"))
print(courselist)

print()
print("################################################")
print()

L = [1, 1, 1, 2, 41, 10 , 15]
N = ["Afraa" , "Noha" , "Haytham" , "Noha", "Soha", "Basmah"]
print(L.count(1))
print(L.count(2))
print(L.count(3))
print(N.count("N"))
print(N.count("Noha"))

print()

print(L.index(2))
#print(L.index(4)) #will give us error
print(N.index("Noha"))
print(L.index(1))

print()

print(list(reversed(L)))
# For string 
seqString = 'geeks'
print(list(reversed(seqString)))
myname = "Afraa"
print(list(reversed(myname)))
# For tuple 
seqTuple = ('g', 'e', 'e', 'k', 's') 
print(list(reversed(seqTuple)))   
# For range 
seqRange = range(1, 5)
print(list(seqRange))
print(list(reversed(seqRange))) 
# For list 
seqList = [1, 2, 4, 3, 5] 
print(list(reversed(seqList)))

print()

L.extend(N)
print(L)

print()

print("N befor sort : " , N)
N.sort()
print("N after sort : " , N)

list_int1 = [ 13, 14, 10, 5, 90, 1]
print("list_int1 befor sort : " , list_int1)
list_int1.sort()
print("list_int1 after sort : " , list_int1)

