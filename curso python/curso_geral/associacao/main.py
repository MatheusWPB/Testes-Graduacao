import classes as cl 

escritor =cl.Escritor('Joãozinho')
caneta = cl.Caneta('Bic')
maquina = cl.MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()

