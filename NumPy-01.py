import numpy as np

a=np.array([[1, 2, 3], [4, 5, 6]])
b=np.array([1, 3, 5, 7], complex)
c=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(a)
print(c)
print(b.ndim)
print(c.itemsize)
print(b.dtype)
print(a.shape)
print(b.shape)
print(a.size)
print(c.size)

d=np.array([[1, 2], [3, 4], [5, 6]])
print("printing the original array")
print(d)

e=d.reshape(2, 3)
print("printing the reshaped array")
print(e)

print(a[0, 2])
print(a[1, 2])
print(a[1, 1])

print(d.max())
print(d.min())
print(d.sum())

print(np.sqrt(d))
print(np.std(d))

e=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
f=np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print(e+f)
print(e*f)
print(e/f)

print(e.max(axis=1))
print(e.max(axis=0))


print(np.vstack((e, f)))
print(np.hstack((e, f)))