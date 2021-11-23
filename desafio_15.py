 def find_missing(vetor):
      dif=[]
      pos=valor=0
      for i in range(1,len(vetor)):
          progressao=vetor[i]-vetor[i-1]
          dif.append(progressao)
      for c in range(len(dif)):

          if dif.count(dif[c]) == 1:
              pos=c

          else:
              valor=dif[c]
      return (vetor[pos] + valor)
