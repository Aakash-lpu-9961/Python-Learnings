print("this is test program")

# for loops in python

list1 = ["Aakash", "Vikash", "Vineet", "Ravi", "Pankaj", "Nitish"]

for p in list1:
    print(p)

list2 = ["Aakash", "Vikash", "Vineet", "Ravi", "Pankaj", "Nitish", "Nimish"]

for q in list2:
    print("This is list2 elements: \t", q)


list3 = [("Aakash", 5), ("Vikash", 6), ("Vineet", 7)]

for r in list3:
    print("This is list3 elements: \t", r)



list4 = [("Aakash", 5), ("Vikash", 6), ("Vineet", 7), ("Shudhanshu", 8)]

for s , t in list4:
    print("This is elements of lists4:\t", s, t)


# Typecasting the list in dictionary


list4 = [("Aakash", 5), ("Vikash", 6), ("Vineet", 7), ("Shudhanshu", 8), ("Yash", 9)]

dict1 = dict(list4)         # typecasting in dictionary from list4

for u in dict1:
    print("elements of dict1:\t", u)

for v, w in dict1.items():
    print(u, v)