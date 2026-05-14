"""
Crea una clase llamada Rectangulo, que tenga el método area() y perimetro(), además de los atributos base y altura
"""
# El método debe imprimir "Hola, mi nombre es {self.nombre}."
class Rectangulo():
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base * 2 + self.altura * 2
    

        
        
# Uso
mi_rectangulo = Rectangulo(altura=5,base=10)
print(f"Área: {mi_rectangulo.area()}")
print(f"Perímetro: {mi_rectangulo.perimetro()}")