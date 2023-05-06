import numpy as np
from tabulate import tabulate
def Sustitucion_directa(D, y):
    n = len(y)
    x = np.zeros(n)    
    for i in range(n):
        x[i] = y[i] / D[i][i]    
    return x

def SustitucionRegresivaU(U,b):    
    nfilas=np.shape(U)[0]
    ncolum=np.shape(U)[1]
    x=np.zeros(nfilas)    
    if nfilas!=ncolum:
        print("No es posible")
    for i in range(nfilas-1,-1,-1):
        x[i]=(b[i]-sum(U[i][k]*x[k] for k in range(i+1,nfilas)))/U[i][i]
    return x 
def SustitucionRegresivaL(L,b):
    nfilas=np.shape(L)[0]
    ncolum=np.shape(L)[1]
    x=np.zeros(nfilas)    
    if nfilas!=ncolum:
        print("No es posible")
    for i in range(nfilas):
        x[i]=(b[i]-sum(L[i][k]*x[k] for k in range(i-1,-1,-1)))/L[i][i]
    return x  

def imprimir_titulo(titulo):
    titulo_cent = titulo.center(50)
    print(f"\n{'='*50}\n{titulo_cent}\n{'='*50}")


    
def MatrizCuadrada(A):
    m,n = np.shape(A)
    if m!=n: # Si A no es cuadrada
        print(" -> [-] La Matriz A no es cuadrada.")
        return False
    else:   # Si A es cuadrada
        return True

    
det=["Determinate :"]
sub=[["Submatrices :"]]
def Regular(A):
    if MatrizCuadrada(A):
        n = np.shape(A[0])
        d = round(np.linalg.det(A),5)
        det.append(d)
        sub[0].append(A)
        if d==0:
            return False
        else:
            return True
    else:
        return False

def Simetrica(A):
    if MatrizCuadrada(A) and np.all(A.T == A):
        return True
    else:
        return False
        
    
def FactorizacionLDLt(A,b):
    '''
    Funcion que primero verifica si es posible factorizar la matriz A en 
    La forma LDL.T y retorna esas dos matrices L y D
    
    Parametros Posicionales:
    A -- Matriz cuadrada de coeficientes del sistema de ecuaciones a resolver
    b -- Vector columna del modelamiento Ax = b
    '''
    # Imprime el título centrado y con una línea debajo
    imprimir_titulo("FACTORIZACION LDL.T")
    print("A:\n",A,"\n---------------------------------------------------")
    # 1) Verificamos las Condiciones
    n = np.shape(A)[0]
    print(" 1) Verificamos si admite descomposicion LDM.T")
    for i in range(1,n+1):
        Sub_Matriz_Principal = A[:i,:i]
        if Regular(Sub_Matriz_Principal)==False:
            print("\t [-] No Admite descomposicion LDM.T")
            return False
    tabla = tabulate(sub, headers=det,  tablefmt='grid')
    print(tabla)
    print("\t [+] Submatrices de A son regulares.")
    print("\t [+] Admite descomposicion LDM.T")
    print("\n 2) Verificamos si es simetrica")
    if Simetrica(A)==False:
        print("\t [-] A no es simetrica")
        print("\t [-] No Admite descomposicion LDL.T")
        print("\t Multiplicamos por A.T :  A.T( Ax = b )   ")
        new_A = np.dot(A.T,A)
        new_b = np.dot(A.T,b)
        FactorizacionLDLt(new_A,new_b)       
        return False
    else:
        print("\t [+] A es simetrica")
        print("\t [+] Admite descomposicion LDL.T")
    print("\n 3) Hallamos el L y D")    
    L = np.zeros((n,n)) # L=0    
    D = np.zeros((n,n)) # D=0
    # LDLt
    L_list = []  # ahora es una lista vacía
    D_list = []  # ahora es una lista vacía
    i_list = []
    for i in range(n):       
        sum0 = sum([L[i][j]*L[i][j]*D[j][j] for j in range (i)])
        D[i][i] = A[i][i] - sum0

        for j in range(i, n):
            sum1 = sum([L[j][k]*L[i][k]*D[k][k] for k in range(i)])
            L[j][i] = (A[j][i] - sum1)/D[i][i]

        L_list.append(np.copy(L))  # copiamos la matriz L para almacenarla en la lista
        D_list.append(np.copy(D))  # copiamos la matriz D para almacenarla en la lista
        i_list.append(i)

    # Creamos la tabla con los datos y la imprimimos
    tabla = tabulate(zip(i_list, L_list, D_list), headers=['i', 'L', 'D'], tablefmt='grid')
    print(tabla)
    print("\n 4) A = LDL.T ")
    # Obtenemos la factorización LDL.T
    h= ['L', 'D','L.T']
    datos=[[L,D,L.T]]
    tabla = tabulate(datos, headers=h, tablefmt='grid')
    print(tabla)
    print("\n 5) Reemplazando  Ax=b -> (LDL.T)x = b\n ")
    print("[+] Aplicando sustitucion Regresiva L ->  L(DL.Tx) = b ") 
    y=SustitucionRegresivaL(L,b)    
    print(tabulate([["y",y.reshape(n,1)]], tablefmt='grid'))
    print("[+] Aplicando sustitucion Directa   D ->  D(L.Tx)  = y ")
    z=Sustitucion_directa(D, y)
    print(tabulate([["z",z.reshape(n,1)]], tablefmt='grid'))
    print("[+] Aplicando sustitucion Regresiva U ->  L.T(x)   = z ")
    x=SustitucionRegresivaU(L.T,z)
    
    print(tabulate([["x",x.reshape(n,1)]], tablefmt='grid'))
    h= ['y', 'z','x']
    datos=[[]]
    datos[0].append(y.reshape(n,1))
    datos[0].append(z.reshape(n,1))
    datos[0].append(x.reshape(n,1))
    print(tabulate(datos,headers=h, tablefmt='grid'))
    print("\n 6) Comprobamos :  ")
    LDLt = np.dot(np.dot(L,D),L.T)
    print("[+] LDL.T :\n", LDLt)
    if np.allclose(A, LDLt, rtol=1e-5):
        print("\n[+] La descomposición LDL.T es correcta.")        
    else:
        print("\n[-] La descomposición LDL.T es incorrecta.")
        return False
    
