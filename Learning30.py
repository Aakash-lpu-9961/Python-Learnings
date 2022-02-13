# Decorators in Python
def function1(num):
    """ This function is created for the purpose of understanding the concept of decorators"""
    if num==0:
        print("False")
    else:
        print("True")

x = int(input("Enter a number x : "))
function1(x)
print(function1.__doc__)

# Definition of Decorators
"""
    [1]. Decorators are a very powerful and useful tool in Python since it allows programmers to 
            modify the behaviour of function or class.
    
    [2]. Decorators allow us to wrap another function in order to extend the behaviour of the 
            wrapped function, without permanently modifying it. 
"""

# What is first class function in Python
"""
    First class objects in a language are handled uniformly throughout. 
    They may be stored in data structures, passed as arguments, or used in control structures. 
    A programming language is said to support first-class functions if it treats functions as first-class objects. 
    Python supports the concept of First Class functions.
"""

# Properties of First Class FUnctions
"""
    [1]. A function is an instance of the Object type.
    [2]. We can store the function in a variable.
    [3]. We can pass the function as a parameter to another function.
    [4]. We can return the function from a function.
    [5]. We can store them in data structures such as hash tables, lists, …
"""

# Functions are objects :
"""Python program to illustrate functions
can be treated as objects"""

def shout(text):
    return text.upper()
# print(shout('Hello'))
yell = shout
del shout
print(yell('Hello'))


#  Functions can be passed as arguments to other functions:
"""Python program to illustrate functions
can be passed as arguments to other functions"""


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(fun):
    """storing the function in a variable"""

    greeting = fun("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)


# Functions can return another function:
"""
 Because functions are objects we can return a function from another function. In the below example, 
 the create_adder function returns adder function.
"""


def create_adder(x):
    def adder(y):
        return x + y

    return adder


# p = create_adder(10)
# print(p)




add = create_adder(15)

print(add(11))






# Another Example :

def outer_func():
    def inner_func():
        return "this is inner_func"
    return inner_func()

var = outer_func()
print(var)





# Another Example :


def square(x):
    def rect(y):
        return x+y
    return rect(10)

var1 = square(20)
print(var1)






# Another Example :



def my_fun1(x):
    def my_fun2(y):
        return x+y
    return my_fun2

rd = my_fun1(10)
print(rd(2))











# Another Example :

