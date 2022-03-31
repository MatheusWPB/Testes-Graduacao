import sympy as sp 

x = sp.symbols ('x')

print (x * x)

print('-'*30)


sp.init_printing()

Lista_Simbolos = ['y','z']

y,z = sp.symbols(Lista_Simbolos)

f_x_y = y**2 + z**3

print(f_x_y)


print('-'*30)


resposta = f_x_y.subs(z,1).subs(y,2)

print (resposta)



print('-'*30)



f_zy = (x+y)**2 + y**2 + 2*x*y + y**2

print (f_zy)

print(sp.simplify(f_zy))