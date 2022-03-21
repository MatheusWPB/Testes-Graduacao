import numpy as np
import matplotlib.pyplot as plt

calc = (3.2-1.86) - ((1 / 4) * 0.526)

x = 889.43 / 1000
S = 0.843
b = 1.86
c_medium = 0.463
AR = 3
teta = np.linspace(np.pi/36, np.pi/18, 20)
# l_ht = 0.67874
cht = np.linspace(.150,.400, 20)
s_it = (cht ** 2) * AR
# bht = (s_it / cht)

V_ht = [0.35, 0.5]


# s_it = np.linspace(0,1,200)
Vht = list(); Sht_old = list(); lht_save = list(); lht_f = list(); Sht_f = list(); teta_save = list()

for k in teta:
    l_ht = (x - cht * (3 / 4)) / np.cos(k)
    for i, S_ht in enumerate(s_it):
        Vht_test = ((l_ht) * S_ht) / (c_medium * S)
        for j in range(0, len(Vht_test)):
            x_test = l_ht[j] * np.cos(k) + (3 / 4) * (S_ht / AR) ** (1 / 2)
            if (Vht_test[j] >= V_ht[0] and Vht_test[j] <= V_ht[1] and x_test <= x and x_test >= x*0.99):
                Vht.append(Vht_test[j])
                Sht_old.append(S_ht)
                lht_save.append(l_ht[j])
                teta_save.append(k)
        
Sht_n = np.array(Sht_old)
lht_n = np.array(lht_save)
print(f'{teta}')
