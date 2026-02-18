# RETO: El Cazador de Duplicados
# Instrucciones: El jugador ha recogido muchos ítems, pero el inventario se ve sucio 
# con tantos repetidos. Convierte la lista a un SET para dejar solo los objetos únicos.

botin_bruto = ["Espada", "Moneda", "Escudo", "Espada", "Moneda", "Gema", "Espada"]
botin_unico = set(botin_bruto)
# TODO: Convierte la lista a un set para eliminar duplicados
# botin_unico = ...
# Tu código aquí:

print(f"Botín limpio: {botin_unico}")
# Observa: ¿Siguen en el mismo orden que la lista original? (Spoiler: No siempre)