list1 = []
print(list1)
list1 = [" "]
print(list1)
list_int = [2, 4, 6, 8]
print(list_int)
list_str = ["Afraa", "Noha", "Leen", "Joudi"]
print(list_str)
list_float = [2.4, 4.75, 8.8]
print(list_float)
list_mix = [2.4 , 7 , "Walaa"]
print(list_mix)

print("##############################")

print(list_str[1]) #Noha
print()

for x in list_str :
    print(x)
print()

for x in list_float:
    print(x)

print("##############################")

list_str[0] = "Afraa_mhm"
print(list_str)
del list_int[0]
print(list_int)
del list_int[1]
print(list_int)
del list_int
print(list_int)
