dec = int (input('Digite um numero inteiro para ser tranformado em binario: '))

#inputs
reste = 0 ; cont = dec ; rest = 0 ; div = 0
#listas

lista = list() ; lista_rest = list() ; lista_result = list()

while div != 1 :

    rest = int(cont % 2)
    div = int (cont / 2)
    lista.append (div)
    lista_rest.append (rest)
    cont = div

for x in range (len(lista)):
    
    lista_result.append (lista_rest[x])

lista_result.append (lista[x])
lista_result.reverse()

print (f'Seu numero {dec} é:  ', end='')
for y in range (len(lista_result)):
    print (f'{lista_result[y]} ', end = '')