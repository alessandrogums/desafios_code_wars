import math
def strongest_even(ini,fim):
    seq=[x for x in range(ini,fim+1)]
    log_max=math.log2(fim)
    val=2**int(log_max)
    if val in seq:
        return val 
    else:
        log_aprox=int(math.log2(fim))
        potencias=[(2**y) + val  for y in range(1,log_aprox)]
        for valor in potencias[::-1]:
            if valor in seq:
                return valor 
