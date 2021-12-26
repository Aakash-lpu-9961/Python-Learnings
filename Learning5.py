# Dictionary in Python
print("Dictionary in Python !!!")

"""In dictionary each key is separated by colon (:), 
the items are separated by commas and the whole
things is enclosed in curly braces { }"""

dict ={'Name': 'Zara', 'Age': '17', 'Class': 'First'}
print(dict)

# Elements of Dictionary can be updated

dict ={'Name': 'Zara', 'Age': '17', 'Class': 'First', 'RegNo': '12015260'}
print(dict)    # dict dictionary is updated now

dict['Age']= 21  # dict updating age of dictionary
dict['School']= 'Manan Vidya Manrakhan Mahto School Ranchi'

print(dict)



# We can either remove individual dictionary elements or clear the entire contents of a dictionary.


dict ={'Name': 'Zara', 'Age': '17', 'Class': 'First', 'RegNo': '12015260'}

del dict['Name']
print(dict)      # removes an particular entry with key name

# dict.clear()    # removes all entries in a dictionary
# print(dict)

# del dict          # deletes an entire dictionary
print(dict)



# There are two important rules of dictionaries in Python

"""RuleNo-01 --- More than one entry per key not allowed"""

dict={'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print("dict[Name] :", dict['Name'])

# O/P = Manni not Zara because here is more than one entry per key rule is violating

dict={'Name': 'Zara', 'Age': 7, 'Age': 21}
print("dict[Age] :", dict['Age'])

# O/P = 21 not 7 because here is more than one entry per key rule is violating in that case
# according to rule it takes last entry


"""RuleNo-02 --- Keys must be immutable"""
# it means we can use strings numbers or tuples as dictionary keys but something like ["Key"] is
# not allowed.

# dict={['Name']: 'Zara', 'Age': 7, 'Age': 21}
# print(dict['Name'])       "This Statement will throws an error because it is violating RuleNo-02


# Important functions associated with Python

dict ={'Name': 'Zara', 'Age': '17', 'Class': 'First', 'RegNo': '12015260'}
dict1 ={'Name': 'Aakash', 'Age': '21', 'Class': 'Second', 'RegNo': '12015261', 'SId': 'ABX'}

print("Length of dict :", len(dict))
print("Length of dict :", len(dict1))

# print(dict + dict1) we can't able to concatenate the dictionary


print(dict.items())
print(dict.values())
print(dict.copy())
print(dict.update(dict1))
print(dict.fromkeys('Age'))