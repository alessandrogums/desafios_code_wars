def  next_bigger(n):
    vet=[]
    while n != 0:
    	resto=n % 10
    	vet.append((resto))
    	n=n // 10 

    for k in range(len(vet)-1):
    	lado_esq=vet[:k+1]
    	lado_esq.sort()
    	for key, val in enumerate(lado_esq):
    		if val > vet[k+1]:
    			tmp=vet[k+1]
    			vet[k+1]=val
    			lado_esq[key]=tmp
    			lado_esq.sort()
    			vet=vet[len(lado_esq):][::-1]
    			tot=vet+lado_esq
    			x=[str(l) for l in tot]
    			y="".join(x)
    			return int(y)


    return -1 
