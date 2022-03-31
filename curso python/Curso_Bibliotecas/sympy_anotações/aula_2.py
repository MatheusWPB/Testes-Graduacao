import sympy as sp
sp.init_printing()#comando para formatar o resultado, mas não sei fazer funcionar

a = sp.Matrix ([[1,2,3],[4,5,5]])
print (a.shape)#linha e colunas da matriz 

print(a)

print('-'*30)


print (sp.Matrix ([[1,2,3],[4,5,5]]).T) #transposta da matriz 

i = sp.eye(4)#matriz idebridade, o argumento é a quantidade de colunas e linhas
print(i)

print('-'*30)

j = sp.zeros(3)#matriz nyla, o argumento são as linhas e colunas

print(j)

print('-'*30)

k = sp.ones(3)#matriz com apenas o n 1, o argumento são as linhas e colunas
print (k)



