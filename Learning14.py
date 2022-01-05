# Practicing Functions and Docstrings concepts in Python
print("Test Program Learning14.py \n\n\n")
# Program to calculate area and perimeter of a rectangle

"""
Area of rectangle = length*breadth
Area of square = (side)^2
Area of circle = pie(r)^2
"""

print("Area and Perimeter Calculator")
print("RECTANGLE \t\t SQUARE \t\t CIRCLE ", "\n\n\n")


print("Area of rectangle")
def arearect(a, b):
    """ This function calculates the area of rectangle """
    arr = (a*b)
    print("Area of rectangle is w/o storing value in any variable :\t", arr)
    return arr


x = input("Enter length of rectangle:\t")
y = input("Enter breadth of rectangle:\t")

v = arearect(int(x), int(y))
print("Area of rectangle is with storing value in any variable :\t", v, "\n")

print(arearect.__doc__, "\n\n")


print("Area of Square")
def areasqr(c):
    """ This function will calculate the area of square"""
    ars = (c*c)
    print("Area of square is w/o storing value in any variable :\t", ars)
    return ars

p = int(input("Enter side length of square:\t"))

q= areasqr(p)
print("Area of square is with storing value in any variable :\t", q, "\n")
print(areasqr.__doc__, "\n\n")


print("Area of Circle")
def areacir(r):
    """This function will calculate the area of circle"""
    arc = 22/7*(r*r)
    print("Area of circle is w/o storing value in any variable :\t", arc)
    return arc

s = float(input("Enter radius of the circle:\t"))

t = areacir(s)
print("Area of circle is with storing value in any variable :\t", t, "\n")
print(areacir.__doc__, "\n\n")