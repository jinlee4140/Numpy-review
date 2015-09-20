import numpy as np

a = np.array([1,2,3])
print type(a)
print a.shape
print a[0], a[1], a[2]

b = np.array([[1,2,3],[4,5,6]])

print b

print b.shape

print b[0,0], b[0,1], b[1,0]



zeros = np.zeros((2,2))
print zeros

ones = np.ones((1,2))
print ones

e = np.full((2,2), 9)
print e

identity = np.eye(2)
print identity

random = np.random.random((2,2))
random

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print a

b = a[:2, 1:3]
print b

print a[0, 1]
print b[0, 0]

row_r1 = a[1, :]    # Rank 1 view of the second row of a  
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a

print row_r1, row_r1.shape
print row_r2, row_r2.shape

#I don't understand the difference between these two shapes.
