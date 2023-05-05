from tabulate import tabulate

def Rango_Representacion(n): 
    header =["n","Positivos","Negativos"]
    datos=[]
    columna=[]
    for n in range(4,n):
        columna.append(n)
        datos.append([n,[0,2**(n-1)-1],[-1,-(2**(n-1))]])
    print(tabulate(datos, header))
