# RETO: El Portero Lógico
# Instrucciones:
# Solo se permite el paso si el usuario cumple UNA de estas dos:
# - Es mayor o igual de 18 años.
# - Tiene 100 o más monedas de oro.

edad = int(input("¿Qué edad tienes? "))
oro = int(input("¿Cuánto oro tienes? "))

if oro >= 100 or edad >= 18:
    print("Pasa")

else:
    print("no pasas")
# TODO: Crea la condición usando IF / ELSE y operadores lógicos
# Tu código aquí: