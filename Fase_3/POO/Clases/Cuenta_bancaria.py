"""
Crea una clase llamada CuentaBancaria, que tenga el método depositar(), 
retirar() y los atributos titular y saldo.
"""
class CuentaBancaria():
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self,deposito):
        self.saldo += deposito
        print(self.saldo)
    def retirar(self,retiro):
        self.saldoinicial = self.saldo
        self.saldo -= retiro
        if self.saldo >0:
            print(self.saldo)
        else:
            print("error")
            self.saldo = self.saldoinicial
# poner el error cuando el valor sea negativo y que guarde el saldo q se puso
# Prueba el código:
mi_cuenta = CuentaBancaria("Julio",100)
print(mi_cuenta.titular)
print(mi_cuenta.saldo)
#print(mi_cuenta.depositar(deposito=50))
mi_cuenta.depositar(deposito=50)

#print(mi_cuenta)
mi_cuenta.retirar(80)
#print(mi_cuenta)
mi_cuenta.retirar(retiro=100) # Esto debería mostrar el error
#print(mi_cuenta)
mi_cuenta.depositar(deposito=10)