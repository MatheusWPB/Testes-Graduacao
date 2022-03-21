class avião():
    def __init__ (self, S, b):
        self.S = S
        self.b = b
    def alongamento(self):
     y = self.b**2 / self.S
     return y


objeto_avião = avião (0.896,1.84)

AR = objeto_avião.alongamento()

print(f'{AR}')


