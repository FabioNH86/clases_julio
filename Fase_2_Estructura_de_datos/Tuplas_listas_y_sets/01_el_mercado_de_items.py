# RETO: Limpieza de Mercancía
# Instrucciones: Un mercader te da una TUPLA con objetos que compró, 
# pero vienen repetidos y desordenados.

mercancia_sucia = ("Pocion", "Escudo", "Pocion", "Espada", "Escudo", "Manzana")

# TODO: Tu código aquí
set_limpio = set(mercancia_sucia)
lista_final = list(set_limpio)
# 3. Ordenar y print
lista_final.sort()

print(f"Mercancía lista para la venta: {lista_final}")