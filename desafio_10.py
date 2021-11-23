def funn(valor, p):
    valor=str(valor)
    obj=[]
    soma=0
    for elem in valor:
        inteiro=int(elem)
        obj.append(inteiro)
    for i in obj:
        soma+=(i**p)
        p+=1
    k=soma/(int(valor))
    if k == int(k):
        return k 
    else:
        return -1 
      
  
print(funn(46288,3))
