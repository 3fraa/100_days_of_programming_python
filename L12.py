txt = " Please, I want {} sandwishes and {} donutes "
a = 5
b = 7
print("Original text  : " , txt)

#First Solution
print("The final text : ", txt.replace("I","we").format(a,b).replace("a","A"))

#Second Solution
x = txt.replace("I","we")
y = x.format(a,b)
z = y.replace("a","A")
print("The final text : ", z)

