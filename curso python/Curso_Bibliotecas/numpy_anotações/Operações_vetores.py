import numpy as np 
'''

.dot() --> Produto escalar entre vetores
.cross() --> Produto vetorial entre os vetores
.inner()  e .outer() --> Produto escalar e vetorial
.linalg.norm() --> modulo de um vetor
.matmul --> multiplicação de matriz
.linalg.det() --> Determinante de uma matriz
.linalg.inv() --> Inversa da matriz
.linalg.eig() --> autovalor e autovetor 
.linalg.solve() --> resolver sistemas do tipo  Ax = b

'''



a = np.array([1,2,3])

np.dot(a,a)

print(np.dot(a,a))
