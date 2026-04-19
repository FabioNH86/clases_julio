"""
Crea una clase Libro y una clase Biblioteca.
La Biblioteca debe guardar una lista de objetos de tipo Libro.
"""
class Libro():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
class Biblioteca():
    def __init__(self,nombre,listalibros=[]):
        self.nombre = nombre
        self.listalibros = listalibros
    def agregar_libro(self,libro):
        libro=[]
        libro.append()
        
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