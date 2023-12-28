import numpy as np
from numpy import array
from numpy.linalg import svd

A = array([[1,2,3], [1,1,2], [2,3,5], [2,2,4], [3,1,4]])

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

# BEM: alternativer Aufruf der Transponierten von V

#print('V=')
#print(np.transpose(VT))

"""
Hier wollen wir nun überprüfen, ob die gefunde
Singulärwertzerlegung stimmt. Dazu müssen wir aus den
Singulärwerten im Array S zunächst eine 5x3-Matrix machen, deren Diagonale
die in S gespeicherten Singulärwerte von A enthält. 
Hierbei gehen wir wie folgt vor: 
Zuerst erzeigen wir eine 3x3-Diagonalmatrix SDGM mit den Singulärwerten
auf der Hauptdiagonalen. Danach ergänzen wir zwei Nullzeilen, um das
gleiche Matrixformat (5x3) wie A zu erreichen.
"""

# Erstelle Diagonalmatirx mit den Werten von S

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

print('\nU.SDGMaugm.VT=')
print(np.dot(np.dot(U,SDGMaugm),VT))

# Anzahl der Nullzeilen, die hinzugefügt werden sollen

anzahl_nullspalten = m-n

SI = array([1/S[0],1/S[1],0])
T = np.diag(SI)

# Erzeuge Nullzeilen (Matrix mit Nullen und gleicher Breite wie die Originalmatrix)

nullspalten = np.zeros((T.shape[0],anzahl_nullspalten))

# Füge Nullspalten zur Matrix T hinzu

T = np.hstack([T, nullspalten])

print('\nT=')
print(T)

# Bilde Produkt V.T.U^T

print()

UT = U.transpose()
print('\nUT=')
print(UT)

P = np.dot(np.dot(V,T),UT)

print('\nPseudoinverse V.T.UT.=')
print(P)




