list_int = [2, 4, 6, 8, 10, 12, 14]
list_str = ["Afraa", "Noha", "Leen", "Joudi"]
list_float = [2.4, 4.75, 8.8]
list_mix = [2.4 , 7 , "Walaa"]

print(list_int[3])
print(list_int[2:6]) # [6, 8, 10 ,12]
print(list_str[1:3]) #['Noha', 'Leen']
print(list_float[0:2]) #[2.4, 4.75]

print("#########################################")

print("Is Afraa in the list_str : " , "Afraa" in list_str)

if "Walaa" not in list_mix :
    print("Walaa not present in list_mix")
else:
    print("Walaa present in list_mix")

if "Laila" not in list_str :
    print("Laila not present in list_str")

print("#########################################")

list_python = ["python"] * 6
print(list_python)

list_num = list_int + list_float
print(list_num)

list_ = list_str + list_mix
print(list_)

    

