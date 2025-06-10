class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo  # Inicializando o saldo corretamente

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        print(f"Saldo disponível: {self.saldo}")

# Solicita um saldo inicial ao usuário
saldo_inicial = float(input("Digite o saldo inicial: "))
conta = ContaBancaria(saldo_inicial)

# Solicita valores de depósito e saque ao usuário
valor_deposito = float(input("Digite o valor a depositar: "))
conta.depositar(valor_deposito)

valor_saque = float(input("Digite o valor a sacar: "))
conta.sacar(valor_saque)

# Exibe o saldo atualizado
conta.ver_saldo()



