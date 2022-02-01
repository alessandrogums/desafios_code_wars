def contar_letras(string):
   dici={}
   vet=[]
   global validos
   validos='abcdefghijklmnopqrstuvwxyz'
   for l in string:
      if l not in dici and l in validos and string.count(l)>1:
            vet.append(l*string.count(l))
            dici[f'{l}']=string.count(l)
            
   #ordenar, de forma decrescente, os elementos do vetor, levando em consideração os seus tamanhos, sem utilizar o .sort()
   for k in range(1,len(vet)):
      for i in range(k,0,-1):
         if len(vet[i]) > len(vet[i-1]):
            vet[i-1],vet[i]=vet[i],vet[i-1]
   #ordenação só nas regiões onde o len é o msm
   comp=list(map(lambda x: len(x),vet))
   y=0
   while y < len(vet) -1 : 
 
      if len(vet[y]) == len(vet[y+1]):
         tamanho=len(vet[y])
         pos_final=len(comp)-(1+ comp[::-1].index(tamanho))
         aux=vet[y:(pos_final)+1]
         aux.sort()
         vet=vet[:y] + aux + vet[pos_final+1:]
         y+=pos_final
      else:
         y+=1
   return vet 
         
      
             
def mix(s1,s2):
   s1=contar_letras(s1)
   s2=contar_letras(s2)
   lista=[]
   comp=list(map(lambda x:len(x),s1))
   comp2=list(map(lambda y:len(y),s2))
   uni_comps=(comp+comp2)
   uni_comps.sort(reverse=True)
   i,j,k=0,0,0
   #organizar a string final, considerando o s1 como primeiro 
   while len(uni_comps)> i :
      valor_atual=uni_comps[i]
      if len(s1) > j:
         while valor_atual== comp[j] :
            lista.append('1:' +s1[j])
            j+=1
            if j>=len(s1):
              break
      if len(s2) > k:      
         while valor_atual ==comp2[k] :
            lista.append('2:'+ s2[k])
            k+=1
            if k>=len(s2):
              break
      i+=1
   #Remoção das posições com letras repetidas, porém com comprimentos diferentes. Inserção da igualdade entre substrings 
   j,k=0,0
   while j < len(lista):
      pos_atual=lista[j]
      k=j+1
      while k < len(lista):
         
         comp=lista[k]
         if comp[2] == pos_atual[2]:
            if len(comp) !=  len(pos_atual):
               lista.pop(k)
               k=j+1
            elif len(comp) == len(pos_atual):
               indi=lista.index(pos_atual)
               lista[indi]='=:' + pos_atual[2:]
               lista.pop(k)
               k=j+1              
         k+=1
      j+=1
   x=0
   comp=list(map(lambda x: len(x),lista))
   eval=[]
  #organização das substrings que começam com =:
   while len(lista) -1  > x:
      if len(lista[x])==len(lista[x+1]):
         tamanho=len(lista[x])
         pos_final=len(comp)-(1+ comp[::-1].index(tamanho))
         aval=''.join(lista[x:pos_final+1])
         cont=0
         if '=:' in aval:
            for z in range(pos_final,x-1,-1):
               if lista[z][0:2] == '=:':
                  eval.append(lista[z])
                  lista.pop(z)
                  cont+=1
            eval.sort()
            for l in eval:
               lista.insert(pos_final+1-cont, l)
               cont=-1
            eval.clear()
            x+=pos_final
      x+=1
   return '/'.join(lista)
