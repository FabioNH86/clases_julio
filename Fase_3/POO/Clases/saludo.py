"""
Crea una clase llamada Persona, que tenga el método saludar() y el atributo nombre
"""
# El método debe imprimir "Hola, mi nombre es {self.nombre}."
class Persona():
    def __init__(self,nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

max = Persona("max")
max.saludar()