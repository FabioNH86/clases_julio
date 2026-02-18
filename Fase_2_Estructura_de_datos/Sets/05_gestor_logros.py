# RETO: Sistema de Logros
# Instrucciones: Los logros son únicos.
# 1. El jugador gana "Primera Sangre" de nuevo (intenta agregarlo y mira si se duplica).
# 2. El sistema detectó un error: quita el logro "Hacker" que se dio por accidente.

logros_actuales = {"Primera Sangre", "Sobreviviente", "Explorador"}

# TODO 1: Usa .add() para agregar "Primera Sangre" otra vez y también "Ganador"
# Tu código aquí:

# TODO 2: Usa .discard() para borrar "Hacker" (Es más seguro que .remove() si no existe)
# Tu código aquí:

print(f"Logros finales del jugador: {logros_actuales}")
# Verifica: "Primera Sangre" solo debe aparecer una vez.