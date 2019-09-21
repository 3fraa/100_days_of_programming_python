List = ["Afraa" , "Amal"]
Tuple = ("Noha" , "Laila")
print("List  = " , List)
print("Tuple = " , Tuple)
print()

List = []
Tuple = ()
print("List  = " , List)
print("Tuple = " , Tuple)
print()

List = [3]
# if we write as follows //Tuple = (3)
#it will look like item not tuple ,so we must add comma 
item = 3
item1 = (3)
Tuple = (3,)
print("List  = " , List)
print("item = " , item)
print("item1 = " , item1)
print("Tuple = " , Tuple)
print()

Tuple1 = (3, 4.3, "Afraa" )
print("Tuple1 = " , Tuple1)

print(Tuple1[2]) # Afraa
print()

for x in Tuple1:
    print(x)
print()

#del Tuple1
#print("Tuple1 = " , Tuple1) #will give us error

print(Tuple1[0:2])
