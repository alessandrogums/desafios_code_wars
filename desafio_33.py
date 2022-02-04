def tower_of_hanoi(rings):
    ring,tot,jogadas=0,0,0
    while rings > ring:
        tot=2*jogadas+1
        jogadas=tot
        ring+=1
    return jogadas
  
 # ou
def tower_of_hanoi(rings):
    return pow(2,rings) -1 
