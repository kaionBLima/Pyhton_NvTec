
class CarrinhoLoja:
    def __init__(self, produtos):
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.produtos.append((produto, quantidade))
            produto.atualizar_estoque(quantidade)
        else:
            print("Quantidade solicitada maior que o estoque disponível.")

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.get_preco()
        return total
    
    def exibir_itens(self):
        if not self.produtos:
            print("Carrinho vazio.")
        for produto, qtd in self.produtos:
            print(f"{produto.nome} x{qtd} - R${produto.preco * qtd:.2f}")
    
    def _esvasiar_carrinho(self):
        self.produtos.clear()
           