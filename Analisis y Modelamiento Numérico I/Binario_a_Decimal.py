def B_D(numero):
    """Funcion que transforma un numero binario a decimal
    
        Parametros posicionales:
        numero -- numero en tipo string    
    """
    d=0
    if "." in numero :
        (entero,decimal)= numero.split(".")
        n = len(entero)        
        for i in range(n):
            d+=int(entero[i])*(2**(n-i-1))
        m = len(decimal)
        for i in range(m):
            d+=int(decimal[i])*(2**-(i+1))
        return d                
    else:        
        n = len(numero)        
        for i in range(n):
            d+=int(numero[i])*(2**(n-i-1))
        return d 
