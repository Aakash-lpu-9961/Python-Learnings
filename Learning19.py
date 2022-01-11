# Scope, Global Variables and Global Keyword


l = 10                                              # Global Variable
def function1(n):
    """ Function for understanding the usage and concept of local variables"""
    l = 5                                           # Local Scope
    m = 8                                           # Local Scope
    print(l , m , "Printed Successfully")

"""
    print statement l = 5 and m = 8 print karega q ki 
    is function ke pas apna value hai l and m ka , isliye 
    ye function pahle apna value ko use karega na ki global wala.
    value ko.
"""

function1("This is Aakash kumar")                   # Calling a function

"""
print(m) - Throws an error because m is a local variable of function1 so we can't use this outside the
function
"""


print("The function1 is", function1.__doc__)



n=5

def function2():
    """ This function is used to demonstrate the usage of global scope and local scope """
    o = 45
    global n
    n = n+45
    print(n)

function2()

print(n)    # Value of n = 50 , because we have updated the value of n by the help of global keyword

"""
    global keyword ham isliye use karte hai jab hame global keyword ke value 
    ko change krna rhta hai inside the function.
    agar ham global keyword ka use ni karenge or direct change krna chahenge global
    variable ka value ko tab hame error show hoga .
"""









def harry():
    x=20

    def rohan():
        global x
        x = 88
    print("before calling rohan()" , x)
    rohan()
    print("after  calling rohan()", x)



harry()
print(x)