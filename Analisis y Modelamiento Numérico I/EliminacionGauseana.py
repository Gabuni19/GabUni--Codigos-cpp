import numpy as np
from tabulate import tabulate

def ElementalC_Fij(n, i, j):
    E = np.eye(n)
    E[i,i], E[j,j] = 0, 0
    E[i,j], E[j,i] = 1, 1
    return E

def Elemental_Fi(n, i, k):
    E = np.eye(n)
    E[i,i] = k
    return E

def Elemental_Fij(n, i, j, k):
    E = np.eye(n)
    E[i,j] = k
    return E 

def findCero(A,i,j):
    p = -1
    for f in range(i,j):
        if (A[f][i-1]!=0):
            p = f
            break
    return p

def SustRegresiva(U,b):
    # Verificar si es triangular superior y cuadrado
    m,n = U.shape
    if m!=n:
        print("Proceso de Sustitucion Regresiva ERROR-[ Matriz no cuadrada ] ")
        return
    if np.array_equal(A, np.triu(A)):
        print("Proceso de Sustitucion Regresiva ERROR-[ Matriz no triangular superior ] ")
        return
    x = np.zeros(m)
    for i in range(m-1,-1,-1):
        suma = 0
        for j in range(i+1,n):
            suma += U[i][j]*x[j]
        x[i] = (b[i] - suma) / U[i][i]
    return x

def EliminacionGaussiana(A,b):
    m,n = A.shape
    M = np.concatenate((A,b), axis = 1 )
    E = [[A,b,M]]
    print(tabulate(E,headers=[["MATRIZ A"],["MATRIZ b"],["MATRIZ AUMENTADA"]],tablefmt='grid'))

    print("\t[+] ELIMINACION GAUSSEANA\n")       
    for i in range(m-1):
        pivote = M[i][i]
        print("Paso 1 : Hallando el pivote !=0")
        print("\t [+]Pivote   : {}".format(pivote))
        print("\t [+]Posicion : ({},{})".format(i,i))
        if pivote == 0:
            print("\t[-] Cambio de filas.")
            p = findCero(M,i+1,n) # Fila del nuevo pivote !=0
            if p == -1:
                print("No se encontro pivote Nulo.")
                return
            else:
                print("\t [+] Nuevo pivote: {}".format(M[p][i]))
                print("\t [+] Posicion : ({},{})".format(p,i))
                Fip = ElementalC_Fij(m,i,p)
                M_aux=M
                M = np.dot(Fip,M)
                pivote = M[i][i]
                h = ["Fip","M","Fip x M"]
                E = [[Fip,M_aux,M]]
                print(tabulate(E,headers=h,tablefmt='grid'))
                
        # Si no es diferente de cero Hacemos cero la columna
        print("Paso 2 : Las matrices elementales")
        header = ["Matriz Aumentada"]
        c=1
        E = [[M]]
        for j in range(i+1,m):
            factor = M[j][i]/pivote
            Fji = Elemental_Fij(m,j,i,-factor)            
            E[0].insert(0,np.copy(Fji))
            header.insert(0,"E"+str(c)+": F_{}{}({})".format(j,i,-factor))
            c+=1
            M = np.dot(Fji,M)
            
        print(tabulate(E,headers=header,tablefmt='grid'))
        print("Paso 3 : Haciendo (0) la columna C[{}]".format(i))
        print(M,"\n\n")
        
            
    U = M[:,:-1]
    b = M[:,-1:]
    x = SustRegresiva(U,b)
    h = ["U","b","Conjunto Solucion"]
    E = [[U,b,x.reshape(m,1)]]
    print("\t -> Por Sustitucion Regresiva")
    print(tabulate(E,headers=h,tablefmt='grid'))
