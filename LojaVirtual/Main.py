from Loja import Loja
from Produto import Produto

loja = Loja()
loja.adicionar_produto(Produto("Camiseta", 50.0, 10))
loja.adicionar_produto(Produto("Tênis", 200.0, 5))
loja.adicionar_produto(Produto("Calça", 120.0, 8))
loja.adicionar_produto(Produto("Jaqueta", 300.0, 3))
loja.adicionar_produto(Produto("Boné", 30.0, 15))
loja.adicionar_produto(Produto("Relógio", 150.0, 7))
loja.adicionar_produto(Produto("Mochila", 80.0, 4))
loja.adicionar_produto(Produto("Óculos", 120.0, 6))


def menu():
    while True:
        print("\n=== Menu da Loja ===")
        print("1. Listar produtos")
        print("2. Adicionar ao carrinho")
        print("3. Ver carrinho")
        print("4. Finalizar compra")
        print("5. Aplicar desconto a produto")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.listar_produtos()
        elif opcao == "2":
            loja.listar_produtos()
            i = int(input("Digite o número do produto: ")) - 1
            quant = int(input("Digite a quantidade: "))
            loja.comprar(i, quant)
        elif opcao == "3":
            loja.ver_carrinho()
        elif opcao == "4":
            loja.finalizar_compra()
        elif opcao == "5":
            loja.listar_produtos()
            i = int(input("Digite o número do produto para aplicar desconto: ")) - 1
            perc = float(input("Percentual de desconto (%): "))
            loja.aplicar_desconto(i, perc)
        elif opcao == "6":
            print("Obrigado por visitar nossa loja!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()