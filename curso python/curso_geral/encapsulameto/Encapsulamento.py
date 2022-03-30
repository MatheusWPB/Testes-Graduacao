'''
atributos

privado usar _

muito privaso usar __ 


'''

class BaseDeDados:

    def __init__(self):

        self._dados = {}

    def inserir_cliente(self,id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}

        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)
        

    def apagar_clientes(self,id):
        del self._dados['clientes'][id]



bd = BaseDeDados()
bd.inserir_cliente(1,'Maria')
bd.inserir_cliente(2,'Mara')
print ('--- ' *30)
bd.lista_clientes()
bd.apagar_clientes(1)
print ('--- ' *30)
bd.lista_clientes()
