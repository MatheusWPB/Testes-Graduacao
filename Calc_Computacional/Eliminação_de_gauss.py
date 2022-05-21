import numpy as np
l = int(input('Insira o número da dimensão da matriz: '))
c = l+1
matriz = np.zeros((l, c))
x = 0
for n in range(0, l):
    for k in range(0, c):
        matriz[n][k] = float(input(f'Digite o termo da linha {n} e coluna {k}: '))
j = 0
cont=0 
z=0
while cont < l-1:
    for i in range(z,l-1): 
        coef = (matriz[i+1][j+cont]) / matriz[z][cont]
        x = matriz[i + 1] - (coef * (matriz[cont]))
        if matriz[i + 1][j+cont] != 0:
            print(x)
            matriz[i + 1] = np.around(x,5)
            print(matriz[i + 1][j+cont])

    cont = cont+1 
    z=z+1 

print(matriz) 