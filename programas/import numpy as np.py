import numpy as np

class ponto():


    def __init__(self, x = 0, y = 0, z = 0):
        try:
            self.x = x[0]
            self.y = y[1]
            self.z = z[2]
        except:
            self.x  = x
            self.y = y
            self.z = z 


    def mostrar (self):
        return self.x
    
    def dist_to(self, ponto_B):
        A = (self.x -ponto_B.x)**2
        B = (self.y - ponto_B.y)**2
        C = (self.z - ponto_B.y)**2

        return np.sqrt(A+B+C)

    def __add__ (self, ponto_B):

        A = (self.x - ponto_B.x)**2
        B = (self.y - ponto_B.y)**2
        C = (self.z - ponto_B.y)**2

        return np.sqrt(A+B+C)












    pass