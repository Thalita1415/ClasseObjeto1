class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Solicita entrada do usuário e converte para float
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

# Criando uma instância de Retangulo com os valores fornecidos
retangulo = Retangulo(largura, altura)

# Exibindo a área calculada
print(f"Área do retângulo: {retangulo.calcular_area()}")
