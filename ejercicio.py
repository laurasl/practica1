class figura():
    def __init__(self):
        pass    
    def calcular_area(self):
        return "Esta figura no posee área"
    def calcular_perimetro(self):
        return "Esta figura no posee perímetro"

class rectangulo(figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.area * self.altura)
    def calcular_perimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro
r1 = rectangulo(3)
print(r1.calcular_area())
print(r1.calcular_perimetro())

class cuadrado(figura):
    def __init__(self. lado):
        super().__init__()
        self.lado = lado
    def calcular_area(self):
        area = self.lado ** 2
        return area
    def calcular_perimetro(self):
        perimetro = 4 * self.lado
        return perimetro
c1 = cuadrado(3)
print(c1.calcular_area())
print(c1.calcular_perimetro())
