def perimeter(num)
    lista=[1,1,2]
    for c in range(num+1):
        
        if c > 2:
            lista.append(lista[c-1]+lista[c-2])
    return 4*(sum(lista))
