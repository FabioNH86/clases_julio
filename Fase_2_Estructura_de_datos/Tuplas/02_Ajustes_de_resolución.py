# RETO 2: Ajustes de Resolución
# Instrucciones: Tienes una tupla con (Ancho, Alto, FPS, Pantalla_Completa).
# Extrae solo la resolución (los dos primeros números) usando slicing.

tupla = (1920,1020,60,True)

# TODO: Usa slicing [:] para obtener solo el ancho y el alto
resolucion = tupla[0:2]

print(f"La resolución del juego es: {resolucion}")