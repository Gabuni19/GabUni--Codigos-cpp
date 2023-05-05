def ConjuntoF(base,mantisa,L,U):
    for i in range(1,(base**(mantisa))):        
        for j in range(L,U+1):           
            num = "0." + bin(i)[2:][::-1].ljust(mantisa,"0") #Funcionaria solo para base 2
            if num[2]!='0':
                exp = base**j
                print("{} x {}**{}".format(num,base,j),end="  --  ")
        print() 
