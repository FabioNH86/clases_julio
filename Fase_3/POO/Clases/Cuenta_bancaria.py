"""
Crea una clase llamada CuentaBancaria, que tenga el método depositar(), 
retirar() y los atributos titular y saldo.
"""


# Prueba el código:
mi_cuenta = CuentaBancaria("Julio", 100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(80)
mi_cuenta.retirar(100) # Esto debería mostrar el error