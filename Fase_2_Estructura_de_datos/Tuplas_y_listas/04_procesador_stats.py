# RETO: Resumen de Equipo
# Instrucciones: Tienes una lista de tuplas. Cada tupla es (Nombre, Nivel).
# Crea una función que recorra la lista y por cada personaje imprima:
# "El jugador [nombre] es nivel [nivel]"

def mostrar_equipo(lista_jugadores):
    # TODO: Usa un bucle FOR para recorrer la lista
    # TODO: Desempaqueta la tupla en cada iteración
    for nombre, nivel in lista_jugadores:
        print(f"El jugador {nombre} es nivel {nivel}")

equipo_pro = [("Aragon", 50), ("Legolas", 45), ("Gimli", 48)]
mostrar_equipo(equipo_pro)