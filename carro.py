class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"{self.marca} {self.modelo} {self.ano}")

# Solicitando informações ao usuário
marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = input("Digite o ano do carro: ")

# Criando uma instância de Carro com os valores inseridos pelo usuário
carro = Carro(marca, modelo, ano)

# Exibindo as informações do carro
carro.exibir_informacoes()



