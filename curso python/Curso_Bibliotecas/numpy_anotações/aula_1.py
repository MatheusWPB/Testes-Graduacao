import numpy as np 

#arrey 

a_1 = np.array ([1,1,1,1])
a_2 = np.array ([[1,1,1,1],[2,2,2,2]])
print(a_1)
print(a_2.shape, a_2.ndim, a_2.dtype)#n° de colunas e linhas, dimensão da array, tipo dos dados

a_3 = np.arange(27).reshape(3,3,3)

print(a_3)