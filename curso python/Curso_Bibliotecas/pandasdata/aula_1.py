import pandas as pd

lista = [1,2,3,4]
lista_a = [ 'a','n', 'c', 'd' ]
lista_2 = [ 1, 2, 3, 4]

series_1 = pd.Series(lista)
series_2 = pd.Series(lista_2, index = lista_a )

print(series_1)
print(series_2)