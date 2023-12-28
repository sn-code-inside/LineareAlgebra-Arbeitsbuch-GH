import numpy as np

A = np.array([[1,2,3], [1,1,2], [2,3,5], [2,2,4], [3,1,4]])

print('A=')
print(A)

np.set_printoptions(formatter={'float':"{0:8.4f}".format})

P = np.linalg.pinv(A)
print('\npinv(A)=')
print(P)

b1 = np.array([5,3,0,0,0])
b2 = np.array([5,3,8,6,5])

print('\npinv(A).b1')
print(P@b1)

print('\npinv(A).b2')
print(P@b2)

print('\nMinimalabstand von b1 zu Bild(A):')
print(np.linalg.norm(A@P@b1-b1,2))



