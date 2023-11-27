
class rectangulo():

    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        print("el area de tu cuadrilatero es: ", self.longitud * self.ancho)

    def calcular_perimetro(self):
        print("El perimetro de tu cuadrilatero es: ",  self.longitud + self.ancho)


Rectangulo = rectangulo(4,6)

print(Rectangulo.calcular_area())
print(Rectangulo.calcular_perimetro())
