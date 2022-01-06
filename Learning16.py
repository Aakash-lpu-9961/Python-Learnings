# File Handling in Python

"""
"r" - Open a file for reading           Default Mode
"w" - Open a file for writing
"x" - Creates a file if not exists
"a" - Add more content to a file
"t" - Text mode                          Default Mode
"b" - Binary mode
"+" - Read and write mod
"""


# Open() , Read() , & Readline() For Reading File


# f =open("Learning1.txt", "rt")

# content = f.read()
# print(content)

# f.close()
import wsgiref.validate

"""for line in f:
    print(line, end=" ")
"""



# readlines() functions are used for reading a whole txt and make them in a list and prints


""" 
print(f.readlines())
"""


# readline() functions are used for reading a line of a file line by line

"""
print(f.readline())
print(f.readline())
print(f.readline())
"""



# Writing and Appending a File

"""
g = open("Learning2.txt", "w")
b = g.write("This is a learning2.txt file and, we are learning File I/O \n")
print(b)
g.close()
"""


"""
h = open("Learning2.txt", "a")
c = h.write("This is a learning2.txt file and, we are learning File I/O in append mode \n")
print(c)
h.close()
"""

# Handle read and write both


"""
i = open("Learning2.txt", "r+")
d = i.read()
print(d)
i.write("Thank You")
print(d)
"""