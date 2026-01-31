# RETO 1: Validador de Nombres de Jugador
# Instrucciones: El nombre debe tener entre 5 y 12 caracteres y NO tener espacios.

def validar_usuario(nombre):
    # TODO: Implementa la lógica aquí
    # Pista: usa len() y el operador 'in'
    pass

# --- PRUEBAS (No tocar) ---
print(validar_usuario("Player1"))    # Debería ser True
print(validar_usuario("Sol"))        # Debería ser False (muy corto)
print(validar_usuario("Admin Master")) # Debería ser False (tiene espacio)