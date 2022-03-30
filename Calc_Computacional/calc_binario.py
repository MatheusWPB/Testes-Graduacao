bi = int(input('Digite um nimero para ser tranformado em decimal: '))

#inputs
q = str(bi) ; dim = int(len(q))

num = 0 ; soma = 0 ; exp = (dim - 1) ; n= 0 ; result = 0; cont = exp

#LISTAS
lista = list() ; lista_2 = list()



for i in range (len(q)):
    a = int(q[i])
    lista.append (a)

while n != dim :

    j = lista[n] * (2**cont)
    n += 1
    cont -= 1
    lista_2.append (j)

for w in range (len(q) - 1):

    result = lista_2[w] + result

final = (lista_2 [exp] * (2**0)) + result

print(final)