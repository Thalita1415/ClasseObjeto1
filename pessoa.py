class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibirDados(self):
        print(f"Nome da pessoa: {self.nome}, Idade: {self.idade}")

# Criando uma instância da classe Pessoa
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
pessoa = Pessoa(nome, idade)

# Imprimindo os dados
pessoa.exibirDados()

