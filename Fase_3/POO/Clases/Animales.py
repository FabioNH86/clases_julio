"""
Crea una clase padre llamada Animal y dos clases hijas (Perro, Gato).
El método hablar() debe comportarse diferente en cada una.
"""
class Animal():
    def __init__(self,nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def hablar(self):
        return "sonidoperro"
    
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def hablar(self):
        return "sonidogato"


# Prueba el código:
mascotas = [Perro("Rex"), Gato("Michi")]

for mascota in mascotas:
    print(f"{mascota.nombre} dice: {mascota.hablar()}")