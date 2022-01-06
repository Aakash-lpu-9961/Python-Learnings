# Try Except Exception Handling In Python

print("Enter num1:\t")
num1=input()
print("Enter num2:\t")
num2=input()

try:
    print("The sum of these two number is", int(num1)+int(num2))

except Exception as d:
    print(d)


print("This line is very important")