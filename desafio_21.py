def pos_average(string):
    tamanho_substring=string.index(',')
    i=0
    p=''
    while i < len(string):
        if string[i]==' ':
            i+=1
        p+=string[i]
        i+=1
    lista=p.split(",")
    combinacoes,total=0,len(lista)-1
    while total >=0:
        combinacoes+=total
        total-=1
    palavra_ini=''
    cont=0
    for indice  in range(len(lista)-1):
        palavra_ini=lista[indice]
        for indi in range(indice+1,len(lista)):
            palavra_atual=lista[indi]
            for letra in range(len(palavra_atual)):
                if palavra_atual[letra] == palavra_ini[letra]:
                    cont+=1
    return round((cont/(combinacoes*tamanho_substring))*100,10)
  
  
