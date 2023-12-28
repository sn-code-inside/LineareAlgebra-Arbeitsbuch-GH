import numpy as np
from numpy import array
from numpy.linalg import svd

A = array([[1,2,3], [1,1,2], [2,3,5], [2,2,4], [3,1,4]])

print('A=')
print(A)

U, S, VT = svd(A)

np.set_printoptions(formatter={'float':"{0:8.4f}".format})

print('\nU=')
print(U)

print('\ndiags of S:')
print(S)

print('\nV^T=')
print(VT)

print('\nV=')
print(VT.transpose())


