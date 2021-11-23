def remove_elem(vetor,indice):
    new_vetor=vetor[:]
    new_vetor.pop(indice)
    return new_vetor 
def two_sum(vetor, objetivo):
    for i in range(len(vetor)):
        novo_vetor=remove_elem(vetor,i)
        for k in range (len(novo_vetor)):
            soma= vetor[i] + novo_vetor[k]
            if soma == objetivo:
                return (i,k+1)
            else:
                soma=0
