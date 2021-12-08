
def give_triang(perimetro_max):
    """como o ângulo de 120 graus é fixo, então coloquei ele como angulo principal para aplicar a lei dos cossenos e ver se existe validação entre todos os lados, através da própria fórmula."""
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

#Para otimizar ainda mais o algoritmo, pode-se utilizar o ponteiro começando do menor lado(eventualmente implementei como z) até o perímetro máx, caso ele ultrapasse, emprega-se o break.
#seguindo a mesma lógica do z, para o y também , porém indo do y+2z<perímetro. Para o maior valor, x, aplica-se a lei dos cossenos para conferir se corresponde e se o somátorio dos lados é menor ou igual ao perímetro máx.
 for z in range(1, per):
        cont=0
        if (2*z > per): 
            break
        for y in range(z,per):
            if (z + 2*y > per): 
                break
            x = (z*z + z*y + y*y)**0.5
            if (x == int(x) and x+y+z <= per):
                cont += 1
