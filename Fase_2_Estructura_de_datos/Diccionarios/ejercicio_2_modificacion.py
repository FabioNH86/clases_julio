# EJERCICIO 2: MODIFICACIÓN DINÁMICA
# 1. Crea un diccionario 'carrito' con un producto y su precio (ej: "pan": 1.50). {}

# 2. Agrega un nuevo producto al carrito (ej: "leche": 1.20) usando asignación directa.

# 3. Modifica el precio del primer producto para que cueste el doble de su valor original.

# 4. Usa .setdefault() para intentar añadir "oferta": True. 
# Luego úsalo otra vez con una clave que ya exista y observa si el valor cambia.

carrito = {"pan": 2, "arroz":1, "pez": 6}
carrito["Leche"] = 7
carrito["pan"] *= 2
carrito.setdefault("oferta",10)
print(carrito)