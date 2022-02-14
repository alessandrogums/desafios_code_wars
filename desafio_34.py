
#Solução Recursiva
arquivo = 'hanoi.resultado'
def escrever_arquivo(texto):
  with open(arquivo,'a') as file:
     file.write(texto)

def hanoi(num,a,b,c):
  if num == 1:
     escrever_arquivo(str(a +' indo para ' +c+ '\n'))
  else:
     hanoi(num-1,a,c,b)
     escrever_arquivo(str(a +' indo para ' +c + '\n'))
     hanoi(num-1,b,a,c)

num = int(input('número de hanoi: '))
hanoi(num,'A','B','C')

#Sol  iterativa

#Em Desenvolvimento 
