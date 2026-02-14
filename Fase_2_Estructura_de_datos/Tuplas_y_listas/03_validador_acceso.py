# RETO: El Guardián del Portal
# Instrucciones: Crea una función 'puede_entrar' que reciba un 'nombre'.
# Dentro de la función hay una TUPLA con nombres de administradores. 
# La función debe retornar True si el nombre está en la tupla, o False si no.

def puede_entrar(usuario):
    admins = ("Aldo", "Julio", "Python_Master")
    # TODO: Usa el operador 'in' para verificar y retornar True o False
    

# Prueba
print(puede_entrar("Aldo"))  # Debería ser True
print(puede_entrar("Hacker")) # Debería ser False