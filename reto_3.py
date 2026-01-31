# RETO 3: El mercader del pueblo
# Instrucciones: Suma el precio total de la lista de compras usando el diccionario.

precios = {
    "espada": 250,
    "pocion": 50,
    "escudo": 150,
    "mapa": 20
}

def calcular_total(lista_compras):
    total = 0
    # TODO: Recorre la lista_compras y suma el valor de cada item 
    # buscando su precio en el diccionario 'precios'.
    return total

# --- PRUEBAS ---
mi_bolsa = ["espada", "pocion", "pocion"]
print(f"Total a pagar: {calcular_total(mi_bolsa)}") # Debería ser 350
