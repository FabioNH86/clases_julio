# RETO: El Buscador de Partidas
# Instrucciones: Tienes dos grupos de jugadores.
# - 'todos_los_jugadores': Todos los que están en el servidor.
# - 'mis_amigos': Tu lista de amigos.
# Encuentra quiénes de tus amigos están conectados ahora mismo (Intersección).

todos_los_jugadores = {"Jugador1", "Slayer99", "Aldo", "NoobMaster", "Fabio"}
mis_amigos = {"Aldo", "Maria", "Fabio", "Pepe"}

# TODO: Usa la intersección (&) o el método .intersection()
# amigos_conectados = ...
# Tu código aquí:

print(f"Amigos listos para jugar: {amigos_conectados}")

# RETO EXTRA: ¿Quiénes de tus amigos NO están conectados? (Diferencia -)
# amigos_offline = ...
# Tu código aquí:

print(f"Amigos offline: {amigos_offline}")