class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} (Estoque: {self.estoque})"