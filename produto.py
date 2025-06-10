class Produto:
    def __init__(self, nome="", preco=0.0, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def input_dados(self):
        self.nome = input("Digite o nome do produto: ")
        self.preco = float(input("Digite o preço do produto: "))
        self.quantidade = int(input("Digite a quantidade do produto: "))

    def calcular_valor_total(self):
        return self.preco * self.quantidade

# Criando um objeto e coletando os dados do usuário
produto = Produto()
produto.input_dados()

print(f"Produto: {produto.nome}")
print(f"Valor total em estoque: {produto.calcular_valor_total()}")

