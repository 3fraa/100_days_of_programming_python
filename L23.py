dic = {"Name":"Afraa", "Year of Birth":1993, "Major":"CE"}

if "Major" in dic:
    print("-Major- is one of the keys in the -dic- dictionary")
print("There is " , len(dic), " items in dic")
print()
dic["Fav color"] = "white"
print(dic)
dic.pop("Year of Birth")
print(dic)
dic.popitem()
print(dic)
del dic["Name"]
print(dic)
#del dic #will give us error
#print(dic)
dic.clear()
print(dic)
