import numpy as np
l = [1, 2, 3, 4, 5, 6, 7]
a=np.asarray(l)
print("This is a list:", a)

p = (1, 2, 3, 4, 5, 6, 7)
b=np.asarray(p)
print("This is a tuple:", b)

q = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10]]
c=np.asarray(q, dtype=object)
print("This is a array using more than on list:", c)

arr = np.arange(0, 20, 2, int)
print("Numpy Arrays within numerical range:", arr)

arr1 = np.linspace(10, 20, 5)
print("The array over the given range is:", arr1)

arr2 = np.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
print("Iterating over the array: ")
for x in np.nditer(arr2):
    print(x, end=' , ')


arr3 = ([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
print("Printing the transpose of the array:")
q= np.transpose(arr3)
print(np.array(arr3))
print(q)


y=10
z=20
print("Binary representation of y ", bin(y))
print("Binary representation of z ", bin(z))

print("Bitwise and of y and z is ", np.bitwise_or(y, z))
print("Bitwise or of y and z is ", np.bitwise_and(y, z))
