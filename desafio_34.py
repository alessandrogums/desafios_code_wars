
#Solução Recursiva
arquivo = 'hanoi.resultado'
def file_write(text):
  with open(arquivo,'a') as file:
     file.write(text)

def hanoi(num,a,b,c):
  if num == 1:
     file_write(str(a +' indo para ' +c+ '\n'))
  else:
     hanoi(num-1,a,c,b)
     file_write(str(a +' indo para ' +c + '\n'))
     hanoi(num-1,b,a,c)

num = int(input('número de hanoi: '))
hanoi(num,'A','B','C')

#Sol  iterativa

#Em Desenvolvimento 
