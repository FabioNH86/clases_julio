# EJERCICIO 4: ELIMINACIÓN DE DATOS {}
# 1. Crea un diccionario 'inventario' con 4 artículos y sus cantidades numéricas.

# 2. Usa .pop() para eliminar un artículo y guarda su valor en una variable. Imprime ese valor.

# 3. Usa la palabra reservada 'del' para borrar otro artículo diferente.

# 4. Usa .popitem() para eliminar el último elemento restante y muestra qué eliminó.

# 5. Imprime el estado final del diccionario (debería quedar solo un elemento).

inventario = {"uno":1 , "dos":2, "tres": 3, "cuatro": 4}

guardar = inventario.pop("uno")
print(guardar)

del inventario["dos"]

guardar2 = inventario.popitem()
print(guardar2)

print(inventario)