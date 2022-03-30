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


class Aluno (Pessoa):
    
    def estudar (self):
        print(f'{self.nomeclasse} está estudando...')


