
def row_sum_odd_numbers(n):
    soma=0
    v=n-1
    while v >= 1:
        soma+=v
        v-=1
    valor_atual=1 + 2*soma
    soma=valor_atual
    for i in range(1,n):
        valor_atual=valor_atual+2
        soma+=valor_atual
    return soma
  
##outra jeito, bem mais otimizado
def row_sum_odd_numbers(n):
    return pow(n,3)
