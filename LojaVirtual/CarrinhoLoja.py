
class CarrinhoLoja:
    def __init__(self, produtos):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.get_preco()
        return total
    
    def _esvasiar_carrinho(self):
        self.produtos = []
           