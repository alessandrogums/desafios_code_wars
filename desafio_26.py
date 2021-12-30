def top_3_words(palavra):
    for k in palavra:
        if k.isalpha()==False and k.isalnum()==False and k!="'":
            palavra=palavra.replace(k," ")
    palavra=palavra.lower().strip()
    vet=palavra.split()
    lista_filtrada=[]
    pos_ini,pos_fin=0,0
    for pal in vet:
        string=''
        i=0
        ref=list(map(lambda y: y=="'",pal))
        if all(ref)==True:
            continue
        else:
            conf_ini=pal[0]=="'"
            while i < len(pal):
                
                if pal[i]!="'":
                    string+=pal[i]
                else:
                   
                    pos_ini,pos_fin=i-1,i+2
                    if i==0:
                        pos_ini,pos_fin=i,i+2        
                    pedaco=pal[pos_ini:pos_fin]
                    aval=list(map(lambda x:x=="'",pedaco))
                    intersec=[False,True,False]==aval
                    intersec2=[False,True,True]==aval or [False,True]==aval 
                    corresp=all(aval)
                    if corresp==False and intersec==False and intersec2==False and conf_ini==True:
                        string+=pedaco
                        i+=1
                        conf_ini=False
                    if intersec:
                        string+=pedaco[pedaco.index("'"):]
                        i+=1
                    if  corresp:
                        pass
                    if intersec2:
                        pedaco=pedaco.replace(pedaco[0],"")
                        string+=pedaco
                        i+=1   
                    
                i+=1
                
        lista_filtrada.append(string[:])
    
    obj,maiores={},[]
    dici={}
    while len(lista_filtrada) != 0:
            max=0
            if len(maiores) >= 3:
                break
            for k,v in enumerate(lista_filtrada):
                dici={v:lista_filtrada.count(v)}
                obj.update(dici)
                qte=lista_filtrada.count(v)
                if k==0:
                    max=qte
                else:
                    if qte>max:
                        max=qte
            
            palavra_maior=''
            for k,v in obj.items():
                
                if v==max:
                    maiores.append(k)
                    palavra_maior=k
                    break
            lista_filtrada=list(filter(lambda x: x!=palavra_maior,lista_filtrada))
            
            obj.clear()
        
    return maiores
