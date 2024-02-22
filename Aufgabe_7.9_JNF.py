import numpy as np
import sympy as sp

A = np.array([[-1, 5, 0, -5], [5, -1, 0, 5], [1, 0, 4, 1], [5, -5, 0, 9]])
M = sp.Matrix(A)

# Berechne Jordan'sche Normalform 

S, J = M.jordan_form()

print('\nA=')
print(A)

print('\nJordansche Normalform, J=')
print(J)

print('\nTransformationsmatrix, S=')
print(S)

print('\nSchönere Ausgabe durch matrix2numpy:')

J = sp.matrix2numpy(J, dtype=int)
S = sp.matrix2numpy(S,dtype=float)

# Inversion von S

Sinverse = np.linalg.inv(S)

print('\nJordansche Normalform, J=')
print(J)

print('\nTransformationsmatrix, S=')
print(S)

print('\nInverse der Transformationsmatrix, S^(-1)=')
print(Sinverse)

print('\nÄhnlichkeitstransformation S^(-1)AS von A mittels S sollte Jordansche Normalform ergeben:')
print(Sinverse@A@S)