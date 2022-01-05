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

print(function.__doc__, "\n\n\n")

"""By help of .__doc__ we can easily know that what the 
objective of the function and why we have created that function"""




# Arbitrary arguments, *args
""" 
If we don't know how many arguments that will be passed into our function, we have to
add * before the parameter name in the function definition.
 """

def my_function(*kids):
    print("The youngest child is " + kids[0])
    print("The youngest child is " + kids[1])
    print("The youngest child is " + kids[2], "\n\n\n")

my_function("Emil", "Tobias", "Linus")


# Default parameter
"""
if we call the function without arguments it uses the default value
"""

def my_function1(country="Norway"):
    print("I am from"+ "\t", country)

my_function1("Sweden")
my_function1("India")
my_function1()              # Takes default value Norway
my_function1("Brazil\n\n")



# Passing List as an Argument

"""
we can send any data types of argument to a function 
(string , number, list, dictionary etc.), and 
it will be treated as same data type inside the function
"""

def my_function2(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function2(fruits)
