import math

class Forma:
    def area(self):
        pass
    
class Quadrado(Forma):
    
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return math.pow(self.lado, 2)
    
class Circulo(Forma):
    
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * (math.pow(self.raio, 2))
    
quadrado = Quadrado(5)
print(quadrado.area())

circulo = Circulo(7)
print(circulo.area())