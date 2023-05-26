def sum_for_list(lst):
  dici_ls={}
  tot_nums=[]
  for i in lst:
        var_arm=i
        j=2 
        fact=set()
        #fatoração do número
        while j * 2 <= abs(var_arm):
            if i % j == 0:
                fact.add(j)
                i //= j
            else:
                j += 1
        
        
        if len(fact) < 2:
          
            dici_ls[abs(var_arm)]=[var_arm]
        else:
          
            for v in fact:
        
                tmp=[]
                if dici_ls.get(v) == None:
                    dici_ls[v] = [var_arm]
                else:
                    tmp=dici_ls[v]
                    tmp.append(var_arm)
                    dici_ls[v]=tmp 
                    
  dici_sort = sorted(dici_ls.items(), key=lambda item: item[0])
  final_ls=[]
  for k in dici_sort:
      final_ls.append([k[0],sum(k[1])])
      
  return final_ls 


 

        
