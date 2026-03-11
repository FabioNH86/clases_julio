# =================================================================
# PROYECTO: SISTEMA DE GESTIÓN DE INVENTARIO "TECH-STORE"
# =================================================================

# 1. VARIABLES Y DATA: 
# Crea una lista llamada 'inventario' que empiece vacía.
# En ella guardaremos diccionarios por cada producto.
inventario = []

# 2. FUNCIONES:
# Define una función llamada 'agregar_producto' que reciba: nombre, precio y stock.
# La función debe crear un diccionario y añadirlo a la lista 'inventario'.
def agregar_producto(nombre, precio, stock):
    # Escribe aquí el código para crear el diccionario y hacer el .append()
    
    diccionario = {"nombre" : nombre, "precio" : precio, "stock" : stock}
    inventario.append(diccionario)
    

# Define una función llamada 'mostrar_inventario'.
# Debe recorrer la lista con un loop y mostrar los detalles de cada producto.
def mostrar_inventario():
    # Si la lista está vacía, imprime "No hay productos".
    # Si tiene datos, usa un bucle for para imprimir cada diccionario.
    if inventario == []:
        print("No hay productos")
    else:
        numeracion = 0
        for i in inventario: 
            numeracion += 1
            print(f"producto {numeracion}", i)



# Define una función llamada 'vender_producto' que reciba el 'nombre' del producto.
def vender_producto(nombre_buscado):
    # 1. Recorre la lista buscando el producto por su nombre.
    # 2. Si lo encuentras, verifica con un condicional si hay stock (stock > 0).
    # 3. Si hay, resta 1 a la cantidad y confirma la venta.
    # 4. Si no hay stock o no existe, avisa al usuario.
    encontrado = False
    for producto in inventario:
        if producto["nombre"].lower() == nombre_buscado.lower():
            encontrado = True
            if producto["stock"] > 0:
                producto["stock"] -= 1
                print("Producto vendido")
            else:
                print("No hay de ese producto")
    if encontrado == False:
        print("no hay de ese producto")


# 3. BUCLE PRINCIPAL (LOOP) Y CONDICIONALES:
# Crea un menú infinito (while True) que permita al usuario elegir:
#   1. Agregar producto (pide los datos con input())
#   2. Ver inventario
#   3. Vender producto
#   4. Salir (usa 'break' para terminar el programa)

print("--- BIENVENIDO A TECH-STORE MANAGEMENT ---")

# Empieza tu bucle while aquí...
while True:
    numero = input("Elegir opcion: \n 1 agregar producto \n 2 ver inventario \n 3 vender producto \n 4 salir")
    numero = int(numero)
    if numero == 1:
        agregar_producto(input("Nombre del producto"), int(input("Precio del producto")), int(input("Stock del producto")))
    elif numero == 2:
        mostrar_inventario()
    elif numero == 3:
        vender_producto(input("Nombre del objeto"))
    elif numero == 4:
        break
    c = input("Quieres continuar Y/N")
    if str(c).lower() == "y":
        continue
    elif str(c).lower() == "n":
        break
