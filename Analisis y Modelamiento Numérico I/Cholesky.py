import numpy as np
from tabulate import tabulate
import math 
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
def DefinidaPositiva(A):
    if MatrizCuadrada(A):
        n = np.shape(A)[0]
        for i in range(1,n+1):
            subMatriz = A[:i,:i]
            d = round(np.linalg.det(subMatriz),5)
            det.append(d)
            sub[0].append(subMatriz)
            if d<=0:
                print("d = {} . No positivo ".format(d))
                return False
        return True
    else:
        return False
        
def Regular(A):
    if MatrizCuadrada(A):
        n = np.shape(A)[0]
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

def MetodoCholesky(A,b):
    '''
    Funcion que verifica Si la matriz es definida positiva.Para luego hacer
    la descomposicion de Cholesky A = G.T(G); Donde G es triangular superior
    Tambien conocido como el descomposicion L(L.T)
    
    Parametros posicionales
    A -- matriz cuadrada que se desea descomponer
    '''
    n = np.shape(A)[0]
    
    imprimir_titulo("Metodo de Cholesky")
    tabla = tabulate([[A]], headers=["Matriz A"],  tablefmt='grid')
    print(tabla)
    #Verficamos que sea cuadrada y definida positiva
    print(" 1) Verificamos que sea Definida Positiva: ")
    condicion1 = DefinidaPositiva(A)
    condicion2 = Simetrica(A)
    if (condicion1): # Esta funcion ya verifica si es cuadrada
        tabla = tabulate(sub, headers=det,  tablefmt='grid')
        print(tabla)
        print("\t [+] A es definida positiva")
    else:
        tabla = tabulate(sub, headers=det,  tablefmt='grid')
        print(tabla)
        print("\t [-] No es definida positiva. Se encontro un determinante No positivo")
        print("\t [-] No admite factorizacion LDM.T")
       
    print("\n 2) Verificamos si es simetrica")
    if condicion2==False:
        print("\t [-] A no es simetrica")
        print("\t [-] No Admite descomposicion G(G.T) ; G es triangular superior")
        print("\t Multiplicamos por A.T :  A.T( Ax = b )   ")
        new_A = np.dot(A.T,A)
        new_b = np.dot(A.T,b)
        return MetodoCholesky(new_A,new_b)
        
    else:
        print("\t [+] A es simetrica")
    
    if (condicion1 and condicion2):
        print("\n\n 3) Luego : ")
        print(" -> [+] A es simetrica y definida Positva")
        print(" -> [+] A admite descomposicion G(G.T)")
        print("\n\n 4) Hallamos el G : ")
        G = np.zeros((n,n))
        G_list = []  # ahora es una lista vacía        
        i_list = []
        for i in range(n):
            # rellenamos la diagonal
            G[i,i] = math.sqrt(A[i,i]-sum([G[k,i]*G[k,i] for k in range(i)]))
            for j in range(i+1,n):
                # rellenamos los elementos por arriba
                G[i,j] = (A[i,j]-sum([G[k,i]*G[k,j] for k in range(i)]))/G[i,i]
            G_list.append(np.copy(G))  # copiamos la matriz L para almacenarla en la lista
            i_list.append(i)
        # Creamos la tabla con los datos y la imprimimos
        tabla = tabulate(zip(i_list, G_list), headers=['i', 'G'], tablefmt='grid')
        print(tabla)
        
        print("\n 5) A = G.T(G) o L(L.T) ")
        # Obtenemos la factorización LDL.T
        h= ['G.T','G']
        datos=[[G.T,G]]
        tabla = tabulate(datos, headers=h, tablefmt='grid')
        print(tabla)
        
        print("\n 6) A = G.T(G) ")        
        print(tabulate([[A,np.dot(G.T,G)]], headers=["A","G.T x  G "], tablefmt='grid'))
        
        print("\n 7) Hallamos la solucion : G.T(G) x = b ")    
        print("\n[+] Aplicando sustitucion Regresiva L ->  G.T(Gx) = b ") 
        y=SustitucionRegresivaL(G.T,b)    
        print(tabulate([["y",y.reshape(n,1)]], tablefmt='grid'))        
        
        print("[+] Aplicando sustitucion Regresiva U ->  G(x)   = y ")
        x=SustitucionRegresivaU(G,y)
        print(tabulate([["x",x.reshape(n,1)]], tablefmt='grid'))        
        return True
    else:
        print("\t [+] No es posible aplicar el Metodo de Cholesky")
        return False
    
    
