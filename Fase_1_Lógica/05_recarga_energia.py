# RETO: Sistema de Carga de Poder
# Instrucciones:
# Mientras la energía sea menor a 50, suma de 5 en 5 e imprime el progreso.
# Al llegar a 50, el bucle debe detenerse.

energia = 0
maximo = 50

# TODO: Crea un bucle WHILE para recargar la energía
# Tu código aquí:
while energia != maximo:
    energia += 5
    print(energia)
print("¡Poder cargado!")