import sympy as sp
from sympy import Matrix

#A = Matrix([[2,1,2,5,4,5], [1,3,6,10,2,0], [1,2,4,7,2,1]])
#A = Matrix([[0,0,1,0,0], [0,0,1,1,0], [0,0,0,0,1]])
#A = Matrix([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]])
A = Matrix([[2,1,2,5,4,5],[1,3,6,10,2,0],[1,2,4,7,2,1]])

print('rref(A)=')
print(A.rref())

print('\nEchelon-Form: rref(A)[0]=')
print(A.rref()[0])

print('\nPivotspalten: rref(A)[1]=')
print(A.rref()[1])

R, PC = A.rref()

print('\nA=')
print(A)
print('\nschöner mit Sympy to Numpy: A=')
M = sp.matrix2numpy(A, dtype=int)
print(M)

print('\nR=')
print(R)

print('\nschöner mit Sympy to Numpy: R=')
M = sp.matrix2numpy(R, dtype=int)
print(M)