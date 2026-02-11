# RETO: Actualizador de Configuración
# Instrucciones: Las configuraciones vienen en una TUPLA (inmutable).
# Crea una función que reciba la tupla, la convierta en lista para 
# cambiar los "FPS" (índice 1) a 120, y retorne una nueva tupla.

def actualizar_fps(config_actual):
    # TODO: Convertir tupla a lista, cambiar valor en índice 1 y retornar tupla
    templist = list(config_actual) 
    templist[1] = 120
    config_nueva = tuple(templist)
    return config_nueva
# Prueba
ajustes = ("Ultra", 60, "Sombras_ON")
ajustes_nuevos = actualizar_fps(ajustes)
print(f"Configuración actualizada: {ajustes_nuevos}") 
# Debería mostrar: ('Ultra', 120, 'Sombras_ON')