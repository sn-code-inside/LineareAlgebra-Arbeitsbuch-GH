import numpy as np

A = np.array([[1,2,3], [1,1,2], [2,3,5], [2,2,4], [3,1,4]])

print('A=')
print(A)

np.set_printoptions(formatter={'float':"{0:8.4f}".format})

print('\npinv=')
print(np.linalg.pinv(A))


