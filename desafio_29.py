def dirReduc(vet):
    i=0
    while i<(len(vet)-1):
        if (vet[i]=="NORTH" and vet[i+1]=="SOUTH") or (vet[i]=="SOUTH" and vet[i+1]=="NORTH"):
           vet.pop(i+1)
           vet.pop(i)
           i=0
        elif (vet[i]=="WEST" and vet[i+1]=="EAST") or (vet[i]=="EAST" and vet[i+1]=="WEST"):
           vet.pop(i+1)
           vet.pop(i)
           i=0
        else:
           i+=1
    
    
    return vet 
