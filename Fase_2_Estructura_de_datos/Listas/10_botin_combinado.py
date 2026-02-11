# RETO: ¡Botín Combinado! (Unión de listas)
# Instrucciones: Une tu inventario con el contenido del cofre encontrado.

inventario_actual = ["Antorcha"]
cofre = ["Oro", "Gema"]

# TODO: Une ambas listas en una nueva llamada 'nuevo_inventario'
# Pista: Puedes usar el operador '+' o el método .extend()
# Tu código aquí:
inventario_actual.extend(cofre)
print(f"Inventario total: {inventario_actual}")
# Debería mostrar: ['Antorcha', 'Oro', 'Gema']