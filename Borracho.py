import random

class Borracho:

    def _init_(self, nombre):
        self.name = nombre

class BorrachoTradicional(Borracho):
    def _init_(self, nombre):
        super()._init_(nombre)
    
    def camina():
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])
