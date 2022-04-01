import numpy as np

pi = np.pi

#Inputs
xlim = 2.5; ylim = 0.6 
AR = 2
S = np.linspace(0.1,0.3)
# teta = np.linspace(0, pi/6)

#Processamento
c = (S / AR) **(1 / 2)
b = (S / c)

y_pos = (ylim - (b/2))
x_pos = xlim - ((3/4) * c)

k = y_pos/x_pos
teta = np.arctan(k)

l  =  y_pos / np.sin (teta)

values = np.array((S, l, teta))
data = np.array((c, b, y_pos, x_pos))

print (values)