from Carrinho import Carrinho

class Loja:
    def __init__(self):
        self.produtos = []
        self.carrinho = Carrinho()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print("\n=== Produtos Disponíveis ===")
        for i, p in enumerate(self.produtos):
            preco = p.preco_com_desconto()
            print(f"{i+1}. {p.nome} - R$ {preco:.2f} - Estoque: {p.estoque} - Desconto: {p.desconto}%")

    def comprar(self, indice, quantidade):
        if 0 <= indice < len(self.produtos):
            produto = self.produtos[indice]
            if quantidade <= produto.estoque:
                produto.estoque -= quantidade
                self.carrinho.adicionar_item(produto, quantidade)
                print("Produto adicionado ao carrinho.")
            else:
                print("Estoque insuficiente.")
        else:
            print("Produto inválido.")

    def aplicar_desconto(self, indice, percentual):
        if 0 <= indice < len(self.produtos):
            self.produtos[indice].aplicar_desconto(percentual)
            print("Desconto aplicado.")
        else:
            print("Produto inválido.")

    def ver_carrinho(self):
        self.carrinho.exibir_carrinho()
