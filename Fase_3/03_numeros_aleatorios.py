# RETO: El Dado Mágico
# Instrucciones: Importa el módulo 'random' pero llámalo 'rd' usando un alias.
# Genera un número aleatorio entre 1 y 6.
import matplotlib.pyplot as plt
import random as rd
resultado = rd.randint(1, 6)

print(f"Lanzaste el dado y salió: {resultado}")