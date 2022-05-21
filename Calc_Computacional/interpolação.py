import pandas as pd 

def Gauss (a):
    '''
    --> valor de a é a quantidade de colunas da matriz
    '''
    lista_1 = []; lista_2 = []; x_0 = []; y_0=[]

    for i in range(a):
        par_1 = float(input(f'Digite o {i+1}° valor da {1}ª coluna da primeira linha da tabela: '))
        par_2 = float(input(f'Digite o {i+1}° valor da {2}ª coluna da segunda linha da tabela: '))
        lista_1.append(par_1)
        lista_2.append(par_2)

    series_1 = pd.Series(lista_2, index = lista_1)

    print (lista_2, lista_1)
    print (series_1)

    for i in range (a):
        x_0.append(lista_1[i])
        y_0.append(lista_2[i])
    
    x = float(input('valor que deseja interpolar:'))

    cof = []
    for k in range(len(lista_1)):
        l=1
        for j in range(len(lista_1)):
            if k != j:
                l *= (x-x_0[j])/(x_0[j]-x_0[k])
        cof.append(l)

    p = 0
    for m in range(len(cof)):
         p += y_0[m] * cof[m]
    
    print (f'p({str(x)})={p}')






a = Gauss(3)  