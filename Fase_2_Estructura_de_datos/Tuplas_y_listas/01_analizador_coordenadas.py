# RETO: El radar de enemigos
# Instrucciones: Crea una función llamada 'analizar_distancias' que reciba 
# una lista de tuplas (coordenadas). La función debe imprimir cuántas 
# coordenadas hay en total y cuál es la primera de la lista.

def analizar_distancias(lista_coords):
    # TODO: Calcula el total de coordenadas usando len()
    # TODO: Accede a la primera tupla de la lista
    size_lista = len(lista_coords)
    firstcoord = lista_coords[0]
    return size_lista, firstcoord
    

# Prueba
puntos_interes_2 = [(10, 20), (45, 12), (0, 5), (100, 80)]
a = analizar_distancias(puntos_interes_2)
print(f"tamaño de tupla;{a[0]}")
print(f"primera coordenada;{a[1]}")