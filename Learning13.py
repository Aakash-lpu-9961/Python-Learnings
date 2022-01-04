# Functions and Docstrings in Python
print("Test Program Learning13.py \n\n\n")

print("Functions in Python\n\n")

print("built-in functions")
a = 9
b = 7
c = sum((a, b))  # built-in function
print("Value of c is: ", c, "\n\n\n\n")

print("User defined functions")


def function(d, e):
    """ This is a function which will calculate average of two numbers"""  # Ye docstring hai comment ni hai
    average = (d + e) / 2
    print(average)  # This function will print the value of average
    return average


""" 
    Lekin agar ham iske value ko kisi variable me store karana chahte hai tb hame return() statement 
    ka use krna hoga
"""



v = function(5, 7)
print("Value of v using return statement:\t", v)

print(function.__doc__)

"""By help of .__doc__ we can easily know that what the 
objective of the function and why we have created that function"""
