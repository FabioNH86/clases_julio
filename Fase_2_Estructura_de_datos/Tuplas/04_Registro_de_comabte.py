# RETO 4: Registro de Combate
# Instrucciones: Tienes un historial de las últimas acciones del jugador.
# 1. Cuenta cuántas veces usó "Ataque".
# 2. Encuentra en qué posición (índice) ocurrió la primera "Curacion".

historial = ("Ataque", "Ataque", "Esquiva", "Ataque", "Curacion", "Ataque")

# TODO: Usa .count() y .index()
veces_ataque = historial.count("Ataque")
posicion_curacion = historial.index("Curacion")
print(f"El jugador atacó {veces_ataque} veces.")
print(f"La primera curación fue en la posición {posicion_curacion}.")