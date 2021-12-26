# Variable in python

var1= 75    # data type = integer
var2= 56    # data type = integer
var3= 20.5  # data type = float
var4= "My name is Aakash Kumar"    # data type = string

# to identify the type of each variables we use type method

print(type(var1))     # data type = integer
print(type(var2))     # data type = integer
print(type(var3))     # data type = float
print(type(var4))     # data type = string

# operation on variables

print(var1 + var2)     # integer + integer = integer
print(var1 + var3)     # integer + float = float
print(var3 + var2)     # float + integer = float
# print(var1 + var4)   # integer + string = Error !!!
# print(var4 + var2)   # string + integer = Error !!!
# print(var3 + var4)   # float + string = Error !!!

"""To Resolve 
This error we have to use typecasting method in which 
we have to change the datatype of one variable in which we want our desired output
Therefore we have to us the method of typecasting in python """

"""
var1= 75    
var2= 56    
var3= 20.5  
var4= "My name is Aakash Kumar
"""""

print("Value of addition of integer and string:", str(var1)+ " " + var4)
print("Value of addition of integer and float by typecasting:", int(var3) + var1) # use of typecasting



# To replicate the given statement various times

print(100* "Hello World \n")


# Taking Input From user by the help of input( ) method


print("Demonstration of input method")

x = input("What is your name:\t")
print("Your Name is:\t", x)

y = input("Enter your ROll No:\t")
print("Your Roll No is:\t", y)

# print(y + 10)

"""Throws an error because input() method accept any input that we give as a string
 So, first fall we have to do typecasting to integer to convert and make use of it"""

print(int(y) + 10)   # Now it throws no error because we have type casted it into an normal integer


