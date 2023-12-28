import numpy as np
from scipy.linalg import lu

# Beispielmatrix

A = np.array([[2,2,2,1],
                   [2,2,3,2],
                   [1,3,4,4],
                   [1,2,2,2]])

# Matrix A

print("Matrix A=")
print(A)

# Führe die LU-Zerlegung durch

P, L, U = lu(A)

# Gib die Ergebnisse aus

print('\nPermutationsmatrix P=')
print(P)
print('\nUntere Dreiecksmatrix L=')
print(L)
print('\nObere Dreiecksmatrix U=')
print(U)
