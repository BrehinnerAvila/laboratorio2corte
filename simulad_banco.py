class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    # Método para depositar
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"{self.titular} ha depositado ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("La cantidad debe ser positiva.")
    # Método para retirar
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"{self.titular} retiró ${cantidad}. Saldo restante: ${self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad debe ser positiva.")
    # Método para consultar el saldo
    def consultar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo}")
# Función que procesa la fila de clientes
def procesar_fila(fila):
    print("\nProcesando clientes en la fila\n")
    for cliente in fila:  # cada cliente trae una acción
        nombre, accion, monto = cliente
        # Crear una cuenta para cada cliente (simple para la simulación)
        cuenta = CuentaBancaria(nombre, 10000)  # saldo inicial fijo
        print(f"Atendiendo a: {nombre}")
        if accion == "deposito":
            cuenta.depositar(monto)
        elif accion == "retiro":
            cuenta.retirar(monto)
        elif accion == "saldo":
            cuenta.consultar_saldo()
        else:
            print("Acción no válida.")
        print()  # salto de línea
                                #    PRGRAMA PRINCIPAL     
#lista de  nombre, acción, monto 
fila_clientes = [
    ["Juan", "deposito", 5000],
    ["Maria", "retiro", 3000],
    ["Carlos", "saldo", 0],
    ["Ana", "retiro", 15000]
]

procesar_fila(fila_clientes)
