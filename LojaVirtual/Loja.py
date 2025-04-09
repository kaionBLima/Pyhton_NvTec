from Produto import Produto
from Carrinho import Carrinho

class Loja:
    def __init__(self):
        self.produtos = []
        self.carrinho = Carrinho()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print("\nProdutos disponíveis:")
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. {produto}")

    def aplicar_desconto(self, indice, percentual):
        if 0 <= indice < len(self.produtos):
            self.produtos[indice].aplicar_desconto(percentual)
            print("Desconto aplicado com sucesso!")
        else:
            print("Produto inválido.")

    def comprar(self, indice, quantidade):
        if 0 <= indice < len(self.produtos):
            produto = self.produtos[indice]
            self.carrinho.adicionar_produto(produto, quantidade)
        else:
            print("Produto inválido.")

    def ver_carrinho(self):
        self.carrinho.ver_itens()

    def finalizar_compra(self):
        total = self.carrinho.calcular_total()
        print(f"Total: R${total:.2f}")
        valor_pago = float(input("Digite o valor pago: R$"))
        if valor_pago >= total:
            troco = valor_pago - total
            print(f"Pagamento realizado com sucesso. Troco: R${troco:.2f}")
            self.carrinho.esvaziar()
        else:
            print("Pagamento insuficiente.")

