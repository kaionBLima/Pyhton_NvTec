from CarrinhoLoja import CarrinhoLoja
from Produto import Produto

class Loja:
    def __init__(self, carrinho):
        self.produtos = []
        self.carrinho = CarrinhoLoja()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for i, produto in enumerate(self.produtos):
            print(f"{i + 1}. {produto}")

    def aplicar_desconto_produto(self, i, percentual):
        if 0 <= i < len(self.produtos):
            self.produtos[i].aplicar_desconto(percentual)
        else:
            print("Produto inválido.")

    def comprar(self):
        total = self.carrinho.calcular_total()
        print(f"Total da compra: R${total:.2f}")
        valor_pago = float(input("Digite o valor pago: R$"))
        if valor_pago >= total:
            troco = valor_pago - total
            print(f"Pagamento realizado. Troco: R${troco:.2f}")
            self.carrinho.esvaziar()
        else:
            print("Pagamento insuficiente.")

    