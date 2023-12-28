import numpy as np

# Typ-I-Umformung

def typI(A,i,j,lam):
    A[j,:] = A[j,:]+A[i,:]*lam
    return(A) 

# Typ-II-Umformung

def typII(A,i,j):
    A[[i, j],:] = A[[j, i],:]
    return(A)

# Typ-III-Umformung

def typIII(A,i,mu):
    for j in range(np.shape(A)[1]):
        A[i,j] *= mu
    return(A)

# Pivotsuche mit erstem nicht-verschwindenden Element ab Diagonalelement; wenn keins vorhanden, dann k=m

def pivotzeile_einfach(A,j):
    k=j
    m=np.shape(A)[0]
    while A[k,j] == 0: 
        k += 1
        if k==m: break
    return k

# Pivotsuche mit betragsgrößtem Element ab Diagonalelement; wenn Null, dann k=m

def pivotzeile(A,j):
    m=np.shape(A)[0]
    k = np.argmax(np.abs(A[j:m,j]))+j    
    if A[k,j]==0: k=m
    return k

# Zeilenreduktionen bis Echelon-Form mit eliminiertem unteren Dreieck

def rref(A,tol):
    m, n = np.shape(A)
    Z = np.eye(m)
    j = 0
    while j<min(m,n): 

#       Zeilentausch mit der ersten Zeile mit Element ungleich Null in Spalte j; Speicherung in Z
        
        k=pivotzeile_einfach(A,j)
        if k != j and k != m : 
            typII(A,k,j) 
            typII(Z,k,j)

#       Elimination des unteren Dreiecks; Speicherung der Umformungen in Z
        
        i = j

        while i<m:
            if A[i,j] != 0:
                for k in range(m)[i+1:]:                     
                    if abs(A[k,j])<tol: 
                        A[k,j]=0
                    else: 
                        l = -A[k,j]/A[i,j]
                        typI(A,i,k,l) 
                        typI(Z,i,k,l) 
            i += 1
        j += 1
     
#   Sortieren der Nichtnullzeilen nach oben

    nnl = []
    for k in range(m): 
        if np.linalg.norm(A[k,:],1)>=tol: nnl.append(k) 
    Rang=len(nnl)
    for k in range(Rang): 
        if nnl[k]!=k: 
            typII(A,k,nnl[k]) 
            typII(Z,k,nnl[k]) 

#   Normieren auf Stufenpivots = 1

    for k in range(Rang):
        for l in range(m):
            if A[k,l]!=0: break
        f=1/A[k,l] 
        typIII(A,k,f)
        typIII(Z,k,f)

    return(A,Z,Rang)

# Hauptprogramm

np.set_printoptions(formatter={'float':"{0:8.4f}".format})

#M = np.array([[0,0,1,1,1],[0,2,4,6,8],[1,0,1,1,1],[0,1,0,2,1],[0,5,6,7,8],[0,8,10,15,17],[1,16,22,32,46]],float)
#M = np.array([[1,2,3,4],[0,1,1,1],[1,3,4,5],[0,0,0,1]],float)
#M = np.array([[1,1,1,1,1],[1,2,2,2,2],[2,3,3,3,3],[2,4,4,2,2]],float)
#M = np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]],float)
#M = np.array([[0,0,1,0,0,0],[0,0,1,0,0,0],[0,1,1,0,0,0],[0,0,0,0,1,0],[0,0,0,1,0,0],[0,0,0,0,0,0]],float)
#M = np.array([[1,2,3,4],[0,1,1,1],[1,3,4,5],[0,0,0,1],[0,0,0,1]],float)
M = np.array([[2,1,2,5,4,5],[1,3,6,10,2,0],[1,2,4,7,2,1]],float)

M_orig = np.copy(M)
Erg = rref(M,1.0e-8)
Z = np.copy(Erg[1])
R = np.copy(Erg[0])
Rang = np.copy(Erg[2]) 

print('\nM_orig=')
print(M_orig)

print('\nRang =',Rang)

print('\nrref(M)=')
print(R)

print('\nZ=')
print(Z)

print('\nKontrolle: Z.M_orig=')
print(np.dot(Z,M_orig))

print('\mNach Elimination des in R verbleibenden Elements in der ersten Zeile und zweiten Spalte zum Vergleich mit Matlab')
print(typI(R,1,0,-R[0,1]))

