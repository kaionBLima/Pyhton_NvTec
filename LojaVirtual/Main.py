from loja import Loja
from produto import Produto

def exibir_menu():
    print("=" * 40)
    print("1 - Exibir produtos")
    print("2 - Adicionar produto ao carrinho")
    print("3 - Aplicar desconto")
    print("4 - Visualizar carrinho")
    print("5 - Finalizar compra")
    print("6 - Sair")
    print("=" * 40)

def menu():
    loja = Loja()
    loja.adicionar_produto(Produto("Notebook", 3500, 5))
    loja.adicionar_produto(Produto("Mouse", 150, 20))
    loja.adicionar_produto(Produto("Teclado", 200, 15))
    loja.adicionar_produto(Produto("Monitor", 1200, 10))
    loja.adicionar_produto(Produto("Impressora", 800, 8))
    loja.adicionar_produto(Produto("Mesa", 500, 12))
    loja.adicionar_produto(Produto("Cadeira", 700, 7))

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print("\n Produtos disponíveis:")
                loja.listar_produtos()

            case "2":
                loja.listar_produtos()
                i = int(input("\nDigite o número do produto: ")) - 1
                if 0 <= i < len(loja.produtos):
                    qtd = int(input("Quantidade: "))
                    loja.carrinho.adicionar_produto(loja.produtos[i], qtd)
                else:
                    print("Produto inválido.")

            case "3":
                loja.listar_produtos()
                i = int(input("\nDigite o número do produto para aplicar desconto: ")) - 1
                if 0 <= i < len(loja.produtos):
                    desc = float(input("Percentual de desconto (%): "))
                    loja.aplicar_desconto_produto(i, desc)
                    print("Desconto aplicado.")
                else:
                    print("Produto inválido.")

            case "4":
                print("\n Itens no carrinho:")
                loja.carrinho.exibir_itens()

            case "5":
                print("\n Finalizando compra...")
                loja.comprar()

            case "6":
                print("Obrigado por usar a loja. Até logo!")
                break

            case _:
                print("Opção inválida. Tente novamente.")

    if __name__ == "__main__":
         menu()
