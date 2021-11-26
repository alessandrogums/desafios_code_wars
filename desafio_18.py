class Sudoku:
    
    
    def __init__(self,matriz):
        self.matriz=matriz

        
        

    def avaliar_coluna(self):
        col=0
        lista=[]
        while col  < 9:
            for lin in range(len(self.matriz)):
                lista.append(self.matriz[lin][col])
            for elem in lista:
                if lista.count(elem) > 1 :
                    return False 
            lista.clear()
            col+=1
        return True 
  
    def avaliar_linha(self):
        for lin in self.matriz:
            for col in range(len(lin)):
                if lin[col] in lin[col+1:]:
                    return False 
        return True 

      
    def grid(self,col_ini,col_final):
        lista_molde=[1,2,3,4,5,6,7,8,9]
        lista_mod=[]
        x,y=0,3
        for k in range (3):
            for c in self.matriz[x:y]:
                lista_mod.extend(c[col_ini:col_final])
            lista_mod.sort()
            if lista_mod != lista_molde:
                return False
            lista_mod.clear()

            x+=3
            y+=3
        return True 
    
    
    
    def grid_completo(self):
        return self.grid(0,3) and self.grid(3,6) and self.grid(6,9)
    
    
        

obj=Sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]])

if obj.avaliar_coluna() == True and obj.avaliar_linha()==True and obj.grid_completo()==True:
    print('Resolução correta!')
else:
    print('resolução incorreta!')


#outros exemplos
# [5, 3, 4, 6, 7, 8, 9, 1, 2], 
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
