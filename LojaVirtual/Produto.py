class Produto:
    def __init__(self, nome, preco, quantidadeEst):
        self.nome = nome
        self.preco = preco
        self.quantidadeEst = quantidadeEst

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco
    
    def get_quantidadeEst(self):
        return self.quantidadeEst

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

    def set_quantidadeEst(self, quantidadeEst):
        self.quantidadeEst = quantidadeEst

    def __str__(self):
        return f'{self.nome} - R${self.preco} - {self.quantidadeEst} unidades'