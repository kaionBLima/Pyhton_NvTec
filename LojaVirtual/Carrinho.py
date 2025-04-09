class Carrinho:
    def __init__(self):
        self.itens = []  # lista de tuplas: (Produto, quantidade)

    def adicionar_produto(self, produto, quantidade):
        if produto.estoque >= quantidade:
            produto.estoque -= quantidade
            self.itens.append((produto, quantidade))
            print(f"{quantidade}x {produto.nome} adicionado ao carrinho.")
        else:
            print("Estoque insuficiente.")

    def ver_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
        else:
            print("Itens no carrinho:")
            for produto, quantidade in self.itens:
                print(f"{produto.nome} - {quantidade}x - R${produto.preco:.2f}")

    def calcular_total(self):
        return sum(produto.preco * quantidade for produto, quantidade in self.itens)

    def esvaziar(self):
        self.itens.clear()