dic = {"Name":"Afraa", "Year of Birth":1993, "Major":"CE"}
print(dic)
print()

x = dic["Name"]
print(x)
y = dic.get("Year of Birth")
print(y)
print()

dic["Name"] = "Laila"
print(dic)
print()

for x in dic:
    print(x)
print()

for x in dic:
    print(dic[x])
print()

for x in dic.values():
    print(x)
print()

print(dic.values())
print()

for x , y in dic.items():
    print(x, y)
print()

print(dic.items())
print()
