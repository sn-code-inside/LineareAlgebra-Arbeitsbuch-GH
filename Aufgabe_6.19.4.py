import numpy as np
from numpy import array
from numpy.linalg import svd

A = array([[3,1,-4], [-3,-1,4], [-3,1,4], [-3,1,4]])

print('A=')
print(A)

U, S, VT = svd(A)

V = VT.transpose()

np.set_printoptions(formatter={'float':"{0:8.4f}".format})

print('\nU=')
print(U)

print('\nDiagonalkomponenten von S:')
print(S)

print('\nV^T=')
print(VT)

print('\nV=')
print(V)

"""
Hier wollen wir nun überprüfen, ob die gefunde
Singulärwertzerlegung stimmt. Dazu müssen wir aus den
Singulärwerten im Array S zunächst eine 4x3-Matrix machen, deren Diagonale
die in S gespeicherten Singulärwerte von A enthält. 
Hierbei gehen wir wie folgt vor: 
Zuerst erzeugen wir eine 3x3-Diagonalmatrix SDGM mit den Singulärwerten
auf der Hauptdiagonalen. Danach ergänzen wir zwei Nullzeilen, um das
gleiche Matrixformat (4x3) wie A zu erreichen.
"""

# Erstelle Diagonalmatrix mit den Werten von S

SDGM = np.diag(S)

print('\nSDGM=')
print(SDGM)

# Anzahl der Nullzeilen, die hinzugefügt werden sollen

m,n = A.shape

print('\nFormat von A: ',n,'x',m) 

anzahl_nullzeilen = m-n

# Erzeuge Nullzeilen (Matrix mit Nullen und gleicher Breite wie die Originalmatrix)

nullzeilen = np.zeros((anzahl_nullzeilen, SDGM.shape[1]))

# Füge Nullzeilen zur Originalmatrix hinzu

SDGMaugm = np.vstack([SDGM, nullzeilen])

print('\nSDGM_augm=')
print(SDGMaugm)

print('\nA=')
print(A)

print('\nU.SDGMaugm.V^T=')
print(np.dot(np.dot(U,SDGMaugm),VT))

