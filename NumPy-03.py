import numpy as np

a=np.array([[10, 2, 3], [4, 5, 60], [70, 8, 9]])
print("Original Matrix")
print(np.matrix(a))

print("Sorting along the columns")
print(np.sort(a))
print("Sorting along the rows")
print(np.sort(a, 0))