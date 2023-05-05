def normalizar(x):
    """Funcion que nomarliza un valor x ala forma : 0.[...]e[...]
    
        Parametros posicionales:
        x -- numero a normalizar
    """
    #Creamos un variable que indique si es positivo
    positivo=1    
    #Si x es un numero negativo pasarlo a positivo
    if x<0:
        x=abs(x)
        positivo=-1;
    
    if x==0: 
        return (0,0);
    elif (x>1):
        t=len(str(int(x)))
        x=x/10**t
        return (positivo*x,10**t)
    else:
        t=len(str(x).split(".")[-1])        
        aux=x*10**t        
        m=len(str(int(aux)))
        x=x*10**(t-m)
        return (positivo*x,10**-(t-m))
