import math

class TrianguloRectangulo():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def hipotenusa(self):
        h=math.sqrt((self.a*self.a)+(self.b*self.b ))
        h = round(h, 2)
        return h

    def __repr__(self):
        return f'Cateto primero: {self.a}, Cateto segundo: {self.b}, Hipotenusa: {self.hipotenusa}'



mitriangulo = TrianguloRectangulo(2, 3)

print(mitriangulo)
