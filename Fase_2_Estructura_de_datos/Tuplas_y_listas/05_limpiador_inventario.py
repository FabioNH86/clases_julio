# RETO: El Limpiador de Duplicados
# Instrucciones: Crea una función 'limpiar_mochila' que reciba una lista de 
# objetos. La función debe:
# 1. Decir cuántas "Pocion" hay en total.
# 2. Ordenar la lista alfabéticamente.
# 3. Retornar la lista ordenada.

def limpiar_mochila(objetos):
    # TODO: Contar pociones, ordenar lista y retornar
    cuenta = objetos.count("Pocion")
    objetos.sort()
    return objetos, cuenta

mi_mochila = ["Espada", "Pocion", "Escudo", "Pocion", "Bota"]
mochila_final = limpiar_mochila(mi_mochila)
print(f"Inventario listo: {mochila_final}")
