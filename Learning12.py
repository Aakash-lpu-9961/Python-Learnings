# Operators in Python
print("This is test program to learn operators in python Learning12")
print("Operators in Python")



"""
Arithmetic Operators
Assignment Operators
Comparison Operators
Logical Operators
Identity Operators
Membership Operators
Bitwise Operators
"""


# 01-Arithmetic Operators

print("Arithmetic Operators")
print("5+6 is:", 5+6)           # Addition Operators
print("5-6 is:", 5-6)           # Subtraction Operators
print("5*6 is:", 5*6)           # Multiplication Operators
print("5/6 is:", 5/6)           # Division Operator
print("5**6 is:", 5**6)         # Exponential Operators (iska matlab 5 ko power 6 se raise kiya jaye)
print("5%6 is:", 5 % 6)         # Modulas Operator (Ye hamko dega remainder)
print("15//6 is:", 15//6, "\n\n\n")        # Floor Operators



# 02-Comparison Operators

print("Comparison Operators")

i =8
print(i==5)
print(i>=5)
print(i<=5)
print(i!=5, "\n\n\n")


# 03-Logical Operators (AND OR NOT)

print("Logical Operators")

a= True
b= False

print("a AND b:", a and b)
print("a OR b:", a or b, "\n\n\n")


# 04-Identity Operators (is and is not operators)


print("Identity Operators")
a =6
b =7
c =7

print(a is b)           # False
print(a is c)           # False
print(b is c)           # True

print(a is not b)       # True
print(a is not c)       # True
print(b is not c, "\n\n\n")       # False



# 05-Membership Operators (in and not in operators)

print("Membership Operators")

inp = input("Enter the input to see in the list:")
print("You entered:", inp)
list1 =[56, 75, 82, 99, 101]
print(inp, "in list1:", int(inp) in list1)
print(inp, "not in list1:", int(inp) not in list1, "\n\n\n")




# 06-Bitwise Operators

print("Bitwise Operators")

"""
Binary Values

    0 = 00
    1 = 01
    2 = 10
    3 = 11
"""

print("1 & 2:\t", 1 & 2)        # Bitwise AND operator represented by &
print("0 | 3:\t", 0| 3)         # Bitwise OR operator represented by |
print("~1:\t\t", ~1)              # Bitwise NOT Operator represented by ~
print("0 ^ 3:\t", 0 ^ 3)        # Bitwise XOR Operator represented by ^