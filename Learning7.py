# If Else statements  and Else-If Statements in Python

var1= 56
var2= 65
var3= int(input("Enter the number:\t"))
print("You have entered : \t", var3)

if var3>var2:
    print("Number is greater than 65\t")
elif var3==var2:
    print("Number is equals to 65\t")
else:
    print("Number is lesser than 65\t")




# "in" and " not in " keywords in python



list1= [6, 8, 10, 12, 14, 16, 18]

print("Enter the number u want to check weather it is present in list1\t")
n = int(input("Enter the number:\t"))

if n in list1:
    print(n, "is in list1 ")
else:
    print(n, "is not in list1")