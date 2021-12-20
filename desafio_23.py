def construir_possibilidades(numero):
    tot_fin=[]
    for valor in numero:
        valor=int(valor)
        vet1,vet=[],[]
        if valor ==0:
            vet=[0,8]
        elif valor ==8:
            vet=[5,7,8,9,0]
        else:
            matriz=[[1,2,3],[4,5,6],[7,9]]
            i=0
            for lin in matriz:
                    if valor in lin:
                        if len(lin)==3:
                            esq,mei,dir=lin
                            if valor==esq:
                                vet1=[esq,mei]
                            elif valor==mei:
                                vet1=[esq,mei,dir]
                            else:
                                vet1=[mei,dir]
                        else:
                            vet1=[valor,8]
                        break
                    i+=1
            pos=''
            alternativas={'inicio':0,'meio':1,'fim':2}
            for k,v in alternativas.items():
                    if i ==v:
                        pos=k
            alternativas_valores={'inicio':[valor+3],'meio':[valor-3,valor+3],'fim':[valor-3]}
            for k,v in alternativas_valores.items():
                    if pos==k:
                        vet=v
        vet.extend(vet1)
        tot=list(map(lambda x:str(x),vet))
        if len(tot_fin)==0:
            tot_fin=tot
        else:
            lista_mut=[]
            for x in tot_fin:
                for  y in tot:
                    string_atual=x+y
                    if string_atual not in lista_mut:
                        lista_mut.append(string_atual)
            tot_fin.clear()
            tot_fin.extend(lista_mut)
                    
    return tot_fin
    
