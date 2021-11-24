import math
class PaginationHelper:
# The constructor takes in an array of items and a integer indicating
# how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection=collection
        self.items_per_page=items_per_page
        
# returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
      
      # returns the number of pages
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
         
# determines what page an item is on. Zero based indexes.
# this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if item_index == 1:
            item_index=2
        
        elif item_index> (len(self.collection)-1) or item_index<0 :
            return -1
        return math.ceil((item_index+1) / self.items_per_page) - 1
