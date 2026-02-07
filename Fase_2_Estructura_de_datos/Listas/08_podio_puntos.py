# RETO: El Podio de Puntos (Slicing)
# Instrucciones: Extrae solo los primeros 3 puntajes para el podio.

scores = [100, 90, 85, 70, 50, 40, 20]

# TODO: Usa slicing [inicio:fin] para sacar los mejores 3
# top_3 = scores[...]
# Tu código aquí:
top_3 = scores[0:3]
print(f"Los ganadores son: {top_3}")
# Debería mostrar: [100, 90, 85]