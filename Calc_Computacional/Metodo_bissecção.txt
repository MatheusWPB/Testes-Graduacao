import math as mt

lista = list () ; lista_2 = list(); a = []; Eo = 1e-1; result = 0; form_result = []

fun = str('x * log(x) - 1')

r = input('Digite o valor do intevalo: ')

for p in range (len(r)):
    if r[p] != ',':
        a.append(int(r[p]))
    else:
        r[p]==''


i = 2; fun_1 = 0; fun_2 = 0; fun_3 = 0

while i > Eo :

    med = (a[0] + a[1])/2


    x = int (a[0]);  y = int(a[1])

    fun_1 = (x * (mt.log10(x))) - 1
    fun_2 = y * mt.log10(y) - 1
    fun_3 = med * mt.log10(med) - 1


    res = fun_1 * fun_3


    if res < 0:
        a[1] = med
    elif res > 0:
        a[0] = med
    
    i = a[1] - a[0]


print(med)





