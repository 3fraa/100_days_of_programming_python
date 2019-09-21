#creat list in two way
print("Q1:")
print()
print("The list (List) in two ways") 
List = ["سرير", "دولاب", "تسريحة", "مرتبة"]
print("List = ", List)
List = list(("سرير", "دولاب", "تسريحة", "مرتبة"))
print("List = ", List)
print()

#apply 4 functions on the List
#1 copy()
newList = List.copy()
print("1- copy(): ")
print(newList)
print()

#2 append()
List.append("كومدينة")
print("2- append(): ")
print(List)
print()

#3 sort()
List.sort()
print("3- sort(): ")
print(List)
print()

#4 pop()
List.pop(2)
print("4- pop(): ")
print(List)  
print()

##############################################
print("######################################")
print()

print("Q2:")
print()

Tuple = ("swift", "python", "java")
print("Tuple:", Tuple)
print("Is python in the Tuple? " , "python" in Tuple)

if "python" in Tuple:
    print("python in Tuple")


    
