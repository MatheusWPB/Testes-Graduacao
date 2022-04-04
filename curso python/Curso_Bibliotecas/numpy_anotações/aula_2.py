#operadores numpy 

import numpy as np

a =  np.sin(np.pi/2) #sempre em radianos, Ex = 90° é igual a pi/2
b = np.cos (np.pi) #sempre em radianos, Ex = 180° é igual a pi

np.inf
np.nan

#operações

a_1 = np.array([[1,2,3]])

a_2 = np.array([[3,4,5]])

a_3 = np.array([3,4,5])

a_1 + 5 #soma todos os valores da matriz ao n°
a_2 * 10 # ,ultiplica cada elemento por elemento 
a_1 * a_2 #multiplica elemento a elemento

a_1.dot(a_2) #mltiplica matricialmente, da maneira matematica 



print(a, b )