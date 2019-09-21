dic = {"Name":"Afraa", "Year of Birth":1993, "Major":"CE"}
print("dic       =", dic)
dicCopy1 = dic.copy()
print("dicCopy1 = ", dicCopy1)
dicCopy2 = dict(dic)
print("dicCopy2 = ", dicCopy2)
print()

dic["Name"] = "Laila"
dicCopy3 = dic
print("dic       =", dic)
print("dicCopy1 = ", dicCopy1)
print("dicCopy3 = ", dicCopy3)
dicCopy3["Name"] = "Walaa"
print("dic       =", dic)
print()

print("Nested Dictionaries")


AsmaDic = {
    "dic1" :
    {
        "Name" : "Asma",
        "Age" : 29
    },
    "dic2" :
    {
        "Name" : "Adel",
        "Age" : 37
    },
    "dic3" :
    {
        "Name" : "Reem",
        "Age" : 5
    }    
}
print("AsmaDic : ", AsmaDic)
print()

dic1 = {"Name" : "Turki", "Age" : 30 }
dic2 = {"Name" : "Laila", "Age" : 23 }
dic3 = {"Name" : "Yoyo", "Age" : 2 }
LailaFamily = {
    "dic1" : dic1,
    "dic2" : dic2,
    "dic3" : dic3
}
print("LailaFamily : " , LailaFamily)
print()

dicAmal = dict(Name = "Amal", Age = 40)
print(dicAmal)

print()
print("###############################################")
print("###############################################")
print("###############################################")
print()

k = {'a', 'e', 'i', 'o', 'u' }
vowels = dict.fromkeys(k)
print(vowels)
print()
k = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(k, value)
print(vowels)
print()
# vowels keys
k = {'a', 'e', 'i', 'o', 'u' }
value = [1]
vowels = dict.fromkeys(k, value)
print(vowels)
# updating the value
value.append(2)
print(vowels)
print()

print("The keys of dic: " , dic.keys())
di = {}
print("The keys of di: " , di.keys())
print()

x = dic.setdefault("Name")
print("x : " , x)
x = dic.setdefault("Nameee")
print("x : " , x)
newValue = dic.setdefault("fav_drink" , "orange")
print("newValue : " , newValue)
print("dic : " , dic)
print()

d = {1: "one", 2: "three"}
d1 = {2: "two"}
d.update(d1)
print(d)
d1 = {3: "three"}
d.update(d1)
print(d)
print()
