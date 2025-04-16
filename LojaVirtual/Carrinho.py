class Carrinho:
    def __init__(self):
        self.itens = []  # lista de tuplas (produto, quantidade)

    def adicionar_item(self, produto, quantidade):
        self.itens.append((produto, quantidade))

    def exibir_carrinho(self):
        if not self.itens:
            print("Carrinho vazio.")
            return
        print("\n=== Carrinho ===")
        for i, (produto, quantidade) in enumerate(self.itens):
            preco_total = produto.preco_com_desconto() * quantidade
            print(f"{i+1}. {produto.nome} - {quantidade} un. - R$ {preco_total:.2f}")

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco_com_desconto() * quantidade
        return total

    def finalizar_compra(self):
        self.itens.clear()
