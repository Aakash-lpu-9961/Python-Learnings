# Python List and List functions in python

mylist =["aakash", "vikash", "nilesh", 56]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
# print(mylist[4]) throws an error

# list can be modify

mylist[0]="Shivam"
mylist[1]="Ravi"
mylist[2]="Dev"
mylist[3]="Ritesh"

print(mylist)

print("Length of list:", len(mylist))


list1 =[65, 56, 89, 78, 45, 90, 95]
print(len(list1))
print(max(list1))
print(min(list1))
print(55 in list1)

list2 =[96, 56, 78, 96, 12, 23, 74]
print(len(list2))
print(max(list2))
print(min(list2))
print(56 in list2)


#print(5*(list1 + list2))


# Methods in List Function

# Method-01 "append"- it simply adds element to the list in the last position of an list

list1.append(63)
list2.append(41)
print(list1)
print(list2)

# Method-02 "count"- it simply count how many times an object occurs in the list

print(list1.count(65))    # returns how many time an particular object is present in the specified list
print(list1.count(56))
print(list1.count(60))

# Method-03 "Reverse"- it simply reverse the object present in the string

print(list1.reverse())
print(list2.reverse())

# Method-04 "index"- it simply returns the lowest index in list that object appears

print(list1.index(56))
print(list1.index(90))
print(list1.index(65))

# Method-05 "insert"- it simply insert elements is list

print(list1)
print(list2)
list1.insert(2, 93)    # iska matlab index 2 par hame 93 insert krna hai
list2.insert(5, 66)    # iska matlab index 5 par hame  66 insert krna hai
print(list1)
print(list2)


# Method-06 "pop"-removes and returns last object or object from list

list1.pop()
list2.pop()
print(list1)
print(list2)

# Method-07 "Remove"- Removes object from the list

list1.remove(89)
list2.remove(78)
print(list1)
print(list2)