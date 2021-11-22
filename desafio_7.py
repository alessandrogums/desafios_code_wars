def digital_root(numero):
    
    soma=99
    primeira_tentativa=True
    while soma > 9:
        if primeira_tentativa:
            y=str(numero)
            primeira_tentativa=False
        else:
            y=str(soma)
        z=[]
        for k in y:
            g=int(k)
            z.append(g)
        soma=sum(z)
        
    return soma 
numero=int(input('digite um numero:'))

print(digital_root(numero))
