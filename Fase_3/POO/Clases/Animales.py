"""
Crea una clase padre llamada Animal y dos clases hijas (Perro, Gato).
El método hablar() debe comportarse diferente en cada una.
"""


# Prueba el código:
mascotas = [Perro("Rex"), Gato("Michi")]

for mascota in mascotas:
    print(f"{mascota.nombre} dice: {mascota.hablar()}")