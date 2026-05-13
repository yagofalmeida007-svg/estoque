# MENU
from cadastro_de_produtos import cadastrar_produto
from registrar_entrada import registrar_entrada
from registrar_saida import registrar_saida
from consultar_estoque import consultar_estoque
from alertar_estoque_baixo import alertar_estoque_baixo


def iniciar_menu():

    while True:

        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Registrar entrada")
        print("3 - Registrar saída")
        print("4 - Consultar estoque")
        print("5 - Alertar estoque baixo")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            preco = float(input("Preço: R$ "))
            quantidade = int(input("Quantidade: "))

            cadastrar_produto(nome, categoria, preco, quantidade)

        elif opcao == "2":

            produto = input("Produto: ")
            quantidade = int(input("Quantidade de entrada: "))

            registrar_entrada(produto, quantidade)

        elif opcao == "3":

            produto = input("Produto: ")
            quantidade = int(input("Quantidade de saída: "))

            registrar_saida(produto, quantidade)

        elif opcao == "4":
             consultar_estoque()

        elif opcao == "5":

            limite = int(input("Limite mínimo: "))

            alertar_estoque_baixo(limite)

        elif opcao == "6":

            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")
