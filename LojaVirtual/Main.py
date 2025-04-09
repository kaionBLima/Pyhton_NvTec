from Loja import Loja
from Produto import Produto

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
    Loja = Loja()
    Loja.adicionar_produto(Produto("Notebook", 3500, 5))
    Loja.adicionar_produto(Produto("Mouse", 150, 20))
    Loja.adicionar_produto(Produto("Teclado", 200, 15))
    Loja.adicionar_produto(Produto("Monitor", 1200, 10))
    Loja.adicionar_produto(Produto("Impressora", 800, 8))
    Loja.adicionar_produto(Produto("Mesa", 500, 12))
    Loja.adicionar_produto(Produto("Cadeira", 700, 7))

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print("\n Produtos disponíveis:")
                Loja.listar_produtos()

            case "2":
                Loja.listar_produtos()
                i = int(input("\nDigite o número do produto: ")) - 1
                if 0 <= i < len(Loja.produtos):
                    qtd = int(input("Quantidade: "))
                    Loja.carrinho.adicionar_produto(Loja.produtos[i], qtd)
                else:
                    print("Produto inválido.")

            case "3":
                Loja.listar_produtos()
                i = int(input("\nDigite o número do produto para aplicar desconto: ")) - 1
                if 0 <= i < len(Loja.produtos):
                    desc = float(input("Percentual de desconto (%): "))
                    Loja.aplicar_desconto_produto(i, desc)
                    print("Desconto aplicado.")
                else:
                    print("Produto inválido.")

            case "4":
                print("\n Itens no carrinho:")
                Loja.carrinho.exibir_itens()

            case "5":
                print("\n Finalizando compra...")
                Loja.comprar()

            case "6":
                print("Obrigado por usar a Loja. Até logo!")
                break

            case _:
                print("Opção inválida. Tente novamente.")

    menu()
