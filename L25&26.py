#Q1:
print("Sol of Q1: " )
Set = {1, 3, 5, 7, 8}
print(Set)
Set.update([4, 8, 12])
print(Set)
Set.remove(8)
print(Set)
Set.clear()
print(Set)
print()

#Q2:
print("Sol of Q2: " )
Dic = {"name":"pigeon", "type":"bird", "skin cover":"feathers"}
print(Dic)
x = Dic.get("type")
print("the value of type is " , x)
#or
x = Dic["type"]
print("the value of type is " , x)
Dic["skin cover"] = "soft"
print(Dic)

