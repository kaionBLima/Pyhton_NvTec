class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.desconto = 0

    def aplicar_desconto(self, percentual):
        self.desconto = percentual

    def preco_com_desconto(self):
        return self.preco * (1 - self.desconto / 100)
