def To_complemento2(numero , bits ):
    """Funcion que pasa un numero entero a su complemento a 2 en
       en binario a partir de una longitud de palabra (bits).
       
       Parametros Posicionales:
       numero -- entero que se desea pasar a complemento a 2 (int)
       bits -- longitud de palabra con la que se trabaja
    
    """
    if(numero >= 0):
        if(numero<=2**(bits-1)-1):            
            b = bin(numero)[2:]     # Almacena el binario de "numero" en b        
            b = b.rjust(bits,"0")   # completa los bits con cero
            return b
        else:
            print("No se puede representar {}>{}.".format(numero,2**(bits-1)-1))
            return -1
    else:
        
        aux = abs(numero)
        if(aux<=(2**(bits-1))):            
            c2 = 2**bits - aux
            c2 = bin(c2)[2:]              
            return c2
        else:
            print("No se puede representar {}>{}.".format(aux,2**(bits-1)))
            return -1
