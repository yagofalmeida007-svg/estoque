estoque = {}

def cadastrar_produto(nome, categoria, preco, quantidade):
    """Registra novo produto no sistema"""

    estoque[nome] = {
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    print(f"{nome} cadastrado com sucesso!")
