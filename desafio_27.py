def same_structure_as(vet,vet1):
    if type(vet) is not list or type(vet1) is not list:
        return False 
    aval=list(map(lambda x:type(x) is list, vet))
    dici={}
    dici['tamanho']=len(aval)
    dici['posicao']=aval

    aval1=list(map(lambda y:type(y) is list,vet1))
    dici1={}
    dici1['tamanho']=len(aval1)
    dici1['posicao']=aval1
    while True in aval or True in aval1:
        pos=[]
        dici,dici1={},{}
        
        for k,v in enumerate(aval):
            if v==True:
                pos.append(k)
            dici['posicao']=pos
        vet_mut=[]
        for i in pos:
            dici[f'tamanho{i}']=len(vet[i])
            vet_mut.extend(vet[i])
        vet=vet_mut
        aval=list(map(lambda x:type(x) is list, vet))
        
        
        pos1=[]
        for k,v in enumerate(aval1):
            if v==True:
                pos1.append(k)
            dici1['posicao']=pos1
    
        vet_mut1=[]
        for i in pos1:
            dici1[f'tamanho{i}']=len(vet1[i])
            vet_mut1.extend(vet1[i])
        vet1=vet_mut1
        aval1=list(map(lambda x:type(x) is list, vet1))
  
        if dici!=dici1:
            return False 

    if dici1==dici:
        return True
    return False  
