# EJERCICIO 5: FUSIÓN E ITERACIÓN PROFESIONAL {}
# 1. Crea dos diccionarios: 'curso_base' (titulo, horas) y 'curso_detalles' (instructor, nivel, horas).
# Nota: Pon un número de horas distinto en cada uno.

# 2. Usa el método .update() para pasar la info de 'curso_detalles' a 'curso_base'.
# Comprueba qué valor de 'horas' se mantuvo al final.

# 3. Recorre el diccionario resultante usando un bucle 'for' y el método .items().
# Imprime cada línea como: "Propiedad: [clave] -> Valor: [valor]".

# 4. Vacía el diccionario por completo usando el método .clear() e imprímelo.

curso_base = {"titulo": "cursochido", "horas": 6}
curso_detalles = {"instructor": "pablo", "nivel":3, "horas":7}

curso_detalles.update(curso_base)

print(curso_detalles)

for key, value in curso_detalles.items():
    print(f"propiedad: {key} -> valor {value}")

curso_detalles.clear()
print(curso_detalles)