print("Hello !!! this is test program")
# Sets in Python
S1 = set([5, 6, 7, 8])
print(type(S1))   # Hence S1 is a set

print(S1)

l = [56, 78, 89, 75]

print(type(l))

S2 = set(l)
print(type(S2))

print(S2)

S2.add(1)
# S2.add(1)   # S2 adds 1 only one time not two times because sets retains only unique values

print(S2)


print("Length of S2:\t", len(S2))
print("Length of S!:\t", len(S1))

# Different types of Functions in Sets

"""
Function-01 add() -   Adds a given elements to a sets 
Function-02 clear() - Removes all elements from the sets
Function-03 copy() -  Returns a shallow copy of a sets
Function-04 union() - Returns a set that has the union of all sets
Function-05 intersection() - Returns a set which has intersection of all sets
Function-06 isdisjoint() - Returns True if sets are disjoint and vice versa
Function-07 issubset()- Returns true if all elements of set A are present on another set B
"""

print("This Set is S1:\t", S1)
print("This Set is S2:\t", S2)

S2= S1.union({1, 75, 78, 56,  89})
print("This Set is S2 after taking union with S1:\t", S2)

S2= S1.intersection({1, 75, 78, 56,  89})
print("This Set is S2 after taking intersection with S1:\t", S2)

S2= S1.isdisjoint({1, 75, 78, 56,  89})
print("Check that is both sets S1 and S2 are disjoint sets or not:\t", S2)

S2= S1.issubset({1, 75, 78, 56,  89})
print("Check that is both sets S1 and S2 are Subsets of each other or not:\t", S2)


