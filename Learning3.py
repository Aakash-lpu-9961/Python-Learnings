# Strings Slicing and other functions in python

mystr= "my name is Aakash Kumar i am from jharkhand and lives in chatra"

print(mystr)

#for finding length of string we use len() method

print(len(mystr))

# various methods of slicing in string

print(mystr[0:4])
print(mystr[0: ])
print(mystr[5:10])
print(mystr[0: : 2])

# Advanced Slicing in Python

print(mystr[-7:-2])

# String functions in Python

print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.endswith("chatra"))
print(mystr.count("i"))
print(mystr.capitalize())
print(mystr.upper())
print(mystr.lower())
print(mystr.find("chatra"))
print(mystr.replace("is", "are"))