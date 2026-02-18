# RETO: Requisitos de Misión
# Instrucciones: Para entrar a la mazmorra necesitas 3 objetos obligatorios.
# Los requisitos son una TUPLA (no cambian).
# El inventario del jugador es una LISTA (cambia).

requisitos = ("Llave Maestra", "Amuleto de Luz", "Mapa del Bosque")
inventario_jugador = ["Antorcha", "Llave Maestra", "Comida", "Cuerda"]

# TODO:
# 1. Convierte ambos a SETS.
# 2. Usa la resta de conjuntos (Requisitos - Inventario) para saber qué le falta.
# 3. Si el set de "faltantes" está vacío, imprime "¡Puedes entrar!". 
#    Si no, imprime "Te falta: [objetos faltantes]".

# Tu código aquí:
set1 = set(requisitos)
set2 = set(inventario_jugador)

resultado = set1 - set2

if resultado == None:
    print("Puedes pasar")
else:
    print(f"Te falta: {resultado}")