# =================================================================
# PROYECTO: SISTEMA DE GESTIÓN DE INVENTARIO "TECH-STORE"
# =================================================================

# 1. VARIABLES Y DATA: 
# Crea una lista llamada 'inventario' que empiece vacía.
# En ella guardaremos diccionarios por cada producto.


# 2. FUNCIONES:
# Define una función llamada 'agregar_producto' que reciba: nombre, precio y stock.
# La función debe crear un diccionario y añadirlo a la lista 'inventario'.
def agregar_producto(nombre, precio, stock):
    # Escribe aquí el código para crear el diccionario y hacer el .append()
    pass


# Define una función llamada 'mostrar_inventario'.
# Debe recorrer la lista con un loop y mostrar los detalles de cada producto.
def mostrar_inventario():
    # Si la lista está vacía, imprime "No hay productos".
    # Si tiene datos, usa un bucle for para imprimir cada diccionario.
    pass


# Define una función llamada 'vender_producto' que reciba el 'nombre' del producto.
def vender_producto(nombre_buscado):
    # 1. Recorre la lista buscando el producto por su nombre.
    # 2. Si lo encuentras, verifica con un condicional si hay stock (stock > 0).
    # 3. Si hay, resta 1 a la cantidad y confirma la venta.
    # 4. Si no hay stock o no existe, avisa al usuario.
    pass


# 3. BUCLE PRINCIPAL (LOOP) Y CONDICIONALES:
# Crea un menú infinito (while True) que permita al usuario elegir:
#   1. Agregar producto (pide los datos con input())
#   2. Ver inventario
#   3. Vender producto
#   4. Salir (usa 'break' para terminar el programa)

print("--- BIENVENIDO A TECH-STORE MANAGEMENT ---")

# Empieza tu bucle while aquí...