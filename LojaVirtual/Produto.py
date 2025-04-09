class Produto:
    def __init__(self, nome, preco, quantidadeEst):
        self.nome = nome
        self.preco = preco
        self.quantidadeEst = quantidadeEst

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

    def atualizar_estoque(self, quantidade):
        if quantidade > self.estoque:
            raise ValueError("Estoque insuficiente.")
        self.estoque -= quantidade

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} - Estoque: {self.estoque}"