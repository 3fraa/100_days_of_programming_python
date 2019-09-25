#Array
Array = ["Afraa", "Noha", "Leen", "Joudi"]
print(Array)
print(Array[1]) #Noha
x = Array[3]
print(x) #Joudi
Array[3] = "Reem"
print(Array)
print("The length of Array is: ", len(Array))

print()

for x in Array:
    print(x)

Array = ["Afraa", "Noha", "Leen", "Joudi", "joudi"]
Array.append("Reem")
print(Array)
Array.pop(2)
print(Array)
Array.remove("Reem")
print(Array)


