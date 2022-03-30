class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def Falar (self):
        print(f'{self.nomeclasse}Falando....')


class Cliente (Pessoa):

    def compra(self):
        print(f'{self.nomeclasse} comprando...')

class ClienteVIP(Cliente):
    
    def falar (self):
        print('Ela substitui o metodo erdado')
    
    def falar_(Cliente):

        super().Falar()
        print('se quiser chamar o metodo para dentro da classe da class mais p´roxima')
    
    def falar_(Cliente):

        Pessoa.Falar()
        print('procurar em uma class espessifica ')


class ClienteVIP2 ():
    def __init__(self, nome, idade, sobrenome ):
        super(). __init__(nome,idade)

        #ou

        Pessoa.__init__(nome , idade )

        self.sobrenome = sobrenome
        




