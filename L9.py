x = "24"
y = "They are " + x
print(y)

"""
#if we write 
x = 24
y = "They are " + x
print(y)
#will give us an error
#but we can use format() method to combine between character and number
#without need to put the number as a string
"""

sis = 3
bro = 2
txt = "my name is Afraa and I have {} sisters"
txt1 = "my name is Afraa, I have {} sisters and {} brothers"
txt2 = "my name is Afraa, I have {1} sisters and {0} brothers"
print(txt.format(sis))
print(txt1.format(sis,bro))
print(txt2.format(bro,sis))
