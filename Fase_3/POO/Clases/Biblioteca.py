"""
Crea una clase Libro y una clase Biblioteca.
La Biblioteca debe guardar una lista de objetos de tipo Libro.
"""


# Prueba el código:
mi_biblioteca = Biblioteca()

# Creamos objetos de la clase Libro
libro1 = Libro("Python para Principiantes", "Julio Codina")
libro2 = Libro("El Quijote", "Miguel de Cervantes")

# Los agregamos a la biblioteca
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

# Mostramos todo
mi_biblioteca.mostrar_catalogo()