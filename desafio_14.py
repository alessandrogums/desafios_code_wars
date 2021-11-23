def is_pangram(string):
    objj=[]
    alfabeto='abcdefghijklmnopqrstuvxz'
    for  i in string:
        if i.isalpha() :
            objj.append(i.lower())
    for c in alfabeto:
        if c not in objj:
            return False
    return True 
