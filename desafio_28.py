def rgb(r,g,b):
    return hex_uni(r) + hex_uni(g) +hex_uni(b)
def hex_uni(num):
    num=min(255,max(num,0))
    hex={0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 
    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    primeiro_num,segundo_num=num//16,num % 16
    return hex[primeiro_num] + hex[segundo_num]
  
