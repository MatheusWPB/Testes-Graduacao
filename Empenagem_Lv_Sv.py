import numpy as np 

'''
Al_max = Altura maxima estabelecida pelo regulamento
Comp_max = Comprimento maximo pelo regulamento
AR =  Alongamento


'''
def Lv_Sv ( Comp_max = 2.5, Al_max = 0.6, AR = 2,S = np.linspace(0.1, 0.3)):
    import numpy as np

    pi = np.pi

    #Processamento
    c = (S / AR) ** (1 / 2)  #largura do pronfudor 
    b = (S / c)  #comprimento do profundor

    Al_final = (Al_max - (b/2))  #Altura final
    Comp_final = Comp_max - ((3/4) * c)  #Comprimento final

    k = Al_final / Comp_final
    teta = np.arctan (k)

    cont_Lv = list()
    Lv = {}

    for i in range (len(Al_final)):
       a = Al_final[1] / np.sin (teta)
       cont_Lv.append (a)
       a = 0
       cont_Lv.append(Lv)
       cont_Lv.clear
       i += 1
        


    values = np.array ((S, Lv, teta)) ; data = np.array ((c, b, Al_final, Comp_final))

    return values, data


a , b = Lv_Sv()
print (a)
print (b)
print (a[1])