from cadastro_de_produtos import estoque
def registrar_saida(produto_id, quantidade):
    """Remove itens do estoque"""

    if produto_id in estoque:

        if estoque[produto_id]["quantidade"] >= quantidade:
            estoque[produto_id]["quantidade"] -= quantidade
            print(f"Saída registrada! Estoque atual: {estoque[produto_id]['quantidade']}")
        else:
            print("Estoque insuficiente!")

    else:
        print("Produto não encontrado!")
