import math
class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection=collection
        self.items_per_page=items_per_page
        
# retorna o número de itens dentro de toda a coleção
    def item_count(self):
        return len(self.collection)
      
      # precisa retornar o número de pág
    def page_count(self):
         return math.ceil(len(self.collection ) / self.items_per_page)

    def page_item_count(self,pagina_indice):
        self.pagina_indice=pagina_indice
        itens=len(self.collection)
        livro=[]
        while (itens // self.items_per_page) > 0:
            itens=itens- self.items_per_page
            livro.append(self.items_per_page)
        livro.append(itens)
        if self.pagina_indice > (len(livro) -1) or self.pagina_indice < 0:
            return -1
        else:
            return livro[pagina_indice]
         
# determina em que página um item está. Índices baseados em zero.Caso o índice não existe, retornará -1
    def page_index(self,item_index):
        if item_index == 1:
            item_index=2
        
        elif item_index> (len(self.collection)-1) or item_index<0 :
            return -1
        return math.ceil((item_index+1) / self.items_per_page) - 1
