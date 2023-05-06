import numpy as np
from tabulate import tabulate

def e(i,n):
    I=np.identity(n)
    return I[:,i-1:i]


def Fila_maximoElement(sub_matriz):
    n = np.shape(sub_matriz)[0] # Numero de filas
    ind = np.argmax(np.abs(sub_matriz))   
    return ind
        
def Formar_P(n,i_actual,j_maximo):
    I = np.identity(n)
    if(i_actual!=j_maximo):
        colum_actual  = I[:,i_actual:i_actual+1].copy()
        I[:,i_actual:i_actual+1]=I[:,j_maximo:j_maximo+1]
        I[:,j_maximo:j_maximo+1]=colum_actual
        return I
    else:
        return I

def FormarAlpha(Subcolumna):
    m,n = np.shape(Subcolumna)
    f_max = Fila_maximoElement(Subcolumna)   
    maximo = Subcolumna[f_max].copy()
    aux = Subcolumna[0].copy()
    for i in range(m):
        if(Subcolumna[i]==maximo):
            Subcolumna[i]=aux
            Subcolumna[0]=maximo
            break    
    for i in range(m):        
        Subcolumna[i]= Subcolumna[i]/maximo      
    
    return Subcolumna
    
def Formar_M(Subcolumna,i,n):
    I = np.identity(n)
    e = I[i:i+1,:]
    s = np.zeros((n,1))
    s_aux = FormarAlpha(Subcolumna)   
    s[i+1:,:]=s_aux[1:,:]
    
    print(" 3) Generamos M{}: I - alpha.e{}".format(i,i+1))
    print(tabulate([[I,s,e]],headers=["I","alpha","e"], tablefmt='grid')) 
    return I-np.dot(s,e)

def imprimir_titulo(titulo):
    titulo_cent = titulo.center(50)
    print(f"\n{'='*50}\n{titulo_cent}\n{'='*50}")
    
def ParletReit(A):
    imprimir_titulo("Metodo de Parlet Reid")
    n =  np.shape(A)[0]
    print(tabulate([["Matriz A",A]], tablefmt='grid'))  
    for i in range(n-2):
        print(" 1) Evaluamos la subcolumna:")
        Subcolumna = A[i+1:,i:i+1] 
        maximo = Fila_maximoElement(Subcolumna)
        print(tabulate([[A,Subcolumna,A[i,i+maximo+1]]],headers=["A","Subcolumna","maximo"], tablefmt='grid'))  
        P = Formar_P(n,i+1,i+maximo+1)
        print(" 2) Generamos P{}: e{} <-> e{}".format(i+1,i+2,i+maximo+2))
        print(tabulate([["P",P]], tablefmt='grid')) 
        M = Formar_M(Subcolumna.astype(float),i+1,n)
        print(" 4) Generamos M{}:".format(i+1))
        print(tabulate([["M",M]], tablefmt='grid')) 
        print(" 5) Hallamos el MP y MP.T :".format(i+1))
        MP = np.dot(M,P)
        MP_T = MP.T
        print(tabulate([[MP,MP_T]],headers=["MP","MP_T"], tablefmt='grid')) 
        print(" 6) Generamos el nuevo A({}):".format(i+1))
        A_aux=A.copy()
        A_aux = np.dot(MP,A_aux)
        A_aux = np.dot(A_aux,MP_T)
        A=A_aux
        print(tabulate([["MP(A{})MP.T".format(i+1),A]], tablefmt='grid')) 
        print()
