# RETO: Podio de Ganadores Únicos
# Instrucciones: Tienes una lista de resultados de partidas. 
# Cada partida es una tupla: (nombre_jugador, puntos).
# Crea una función que reciba esta lista y devuelva un SET con los nombres 
# de los jugadores que hicieron MÁS de 50 puntos.

def obtener_ganadores(resultados):
    ganadores = set() # Creamos un set vacío
    # TODO: Recorre la lista con un for
    # TODO: Si los puntos (índice 1 de la tupla) > 50, agrega el nombre al set
    return ganadores

# Datos de prueba
partidas = [("Aldo", 60), ("Fabio", 40), ("Julio", 85), ("Aldo", 90), ("Pepe", 30)]

resultado_final = obtener_ganadores(partidas)
print(f"Jugadores destacados (sin repetir): {resultado_final}")
# Debería mostrar: {'Aldo', 'Julio'}