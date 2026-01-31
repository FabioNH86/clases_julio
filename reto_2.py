import random

# RETO 2: Sistema de Daño Crítico
# Instrucciones: Si el número aleatorio (1-10) es 9 o 10, el daño es doble.
# De lo contrario, el daño es el valor base.

def calcular_golpe(danio_base):
    suerte = random.randint(1, 10)
    if suerte > 8:
        danio_base *= 2
        print("¡Crítico!")
        return danio_base
    else:
        return danio_base
    # TODO: Si suerte > 8, devolver danio_base * 2 e imprimir "¡Crítico!"
    # De lo contrario, devolver solo danio_base
    

# Prueba tu función
print(f"Resultado del golpe: {calcular_golpe(50)}")