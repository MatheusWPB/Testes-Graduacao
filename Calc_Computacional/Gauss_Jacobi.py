import numpy as np

k = 2
teste = 200
matriz = np.zeros((3, 4))
x = np.zeros((3,1))
x_ = np.zeros((3,1))
x_max = []
stop = []

E = float(input("Digite o valor da precisão requerida: "))

for i in range(3):
    for j in range(4):
        matriz[i][j] = int(input(f"Digite digite o valor na linha {i+1} e coluna {j+1}: "))

for i in range (3):
    for j in range (1):
        x[i][j] = float(input(f"Digite o valor {i+1} da matriz x0: "))

while k != 0:
    x_[0][0] = float((matriz[0][3]-(matriz[0][2] * x[2][0])-(matriz[0][1] * x[1][0]))/matriz[0][0])
    x_[1][0] = float((matriz[1][3]-(matriz[1][2] * x[2][0])-(matriz[1][0] * x[0][0]))/matriz[1][1])
    x_[2][0] = float((matriz[2][3]-(matriz[2][1] * x[1][0])-(matriz[2][0] * x[0][0]))/matriz[2][2])

    for i in range (3):
        stop.append(abs(x-[i][0]-x[i][0]))
    stop.sort()

    for i in range (3):
        x_max.append(abs(x-[i][0]))
    x_max.sort()

    x[0][0] = x-[0][0]
    x[1][0] = x-[1][0]
    x[2][0] = x-[2][0]

    teste = stop[2]/x_max[2]

    if teste < E:
        k = 0

print(x)