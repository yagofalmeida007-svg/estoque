from cadastro_de_produtos import estoque
def alertar_estoque_baixo(limite):
    """Identifica produtos com estoque crítico"""

    print("\n--- ESTOQUE BAIXO ---")

    encontrou = False

    for produto, dados in estoque.items():

        if dados["quantidade"] <= limite:
            print(f"{produto} -> Quantidade: {dados['quantidade']}")
            encontrou = True

    if not encontrou:
        print("Nenhum produto com estoque baixo.")
