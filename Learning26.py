# Enumerate Functions In Python

l1 = ("Chocolates", "Candies", "Fruits", "Samosa", "Chicken")

# i = 1
# for item in l1:
#     if i % 2 is not 0:
#         print(f" Jarvis please buy {item}")
#     i+=1


#  Using enumerate functions in Python

for ind , item in enumerate(l1):
    if ind%2==0:
        print(f"Jarvis please buy {item}")



l2 = ["eat", "sleep", "repeat"]
s1 = ["geek"]

obj1 = enumerate(l2)
obj2 = enumerate(s1)

print("Return Type:", type(obj1))
print(list(enumerate(l2)))

print(list(enumerate(s1, 2)))        # changing start index to 2 from 0