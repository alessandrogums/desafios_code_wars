
#como o ângulo de 120 graus é fixo, então coloquei ele como angulo principal para aplicar a lei dos cossenos e ver se existe validação entre todos os lados, através da própria fórmula.
def give_triang(perimetro_max):
    ang_principal=-0.5
    cont=0
    for x in range(int(perimetro_max/2),1,-1):
        for y in range(1,x-1):
            z=1
            while x+y+z<=perimetro_max :
                if (x**2)==(y**2)+(z**2) -2*(y*z)*ang_principal and y<z:
                    cont+=1
                z+=1
    return (cont)
print(give_triang(80))
