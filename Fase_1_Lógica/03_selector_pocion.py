# RETO: Sistema de Inventario
# Instrucciones:
# Usa IF, ELIF y ELSE para reaccionar a la poción elegida:
# "roja" -> "Curaste Vida", "azul" -> "Recuperaste Mana", "verde" -> "Subió Energía"
# Cualquier otra cosa -> "Poción desconocida"

print("Pociones disponibles: roja, azul, verde")
eleccion = input("¿Qué poción usas? ").lower()

# TODO: Implementa la lógica de selección aquí
# Tu código aquí:
if eleccion == "roja":
    print("Curaste vida")
elif eleccion == "azul":
    print("Recuperaste mana")
elif eleccion == "verde":
    print("Subio energia")
else:
    print("Pocion desconocida")