def move_zeros(array):
    cont=qte=0

    while cont +1  <= len(array) :

        if array[cont] == 0 :
            array.pop(cont)
            qte+=1
            cont=0

        cont+=1  

    for k in range(qte):
        array.append(0)
    
    if  len(array)>0 and array[0]==0:
        array.pop(0)
        array.append(0)
    
    return array

#outra forma de se fazer
def move_zeros(lista):
    for k in range(len(lista)):
        if lista[k]==0:
            lista.insert(len(lista),0)
            lista.remove(0)
    
    return lista

#mais outra forma 
def move_zeros(array):
    qte=array.count(0)
    array=list(filter(lambda x:x!=0 , array))
    return array + [0]*qte 
