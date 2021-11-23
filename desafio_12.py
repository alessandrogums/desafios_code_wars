def narcissistic(numero):
    numero_copia=numero
    dig=0
    while numero > 0:
        numero=numero//10
        dig+=1
    numero_copia=str(numero_copia)
    vetor=[int(i) for i in numero_copia]
    num_narc=sum(list(map(lambda x:(x**dig) ,vetor)))
    if int(numero_copia) == num_narc:
        return True
    return False 


print(narcissistic(1652))
