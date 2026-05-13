from cadastro_de_produtos import estoque
def consultar_estoque(produto_id):
    """Verifica saldo atual do produto"""

    if produto_id in estoque:

        dados = estoque[produto_id]

        print("\n--- DADOS DO PRODUTO ---")
        print(f"Produto: {produto_id}")
        print(f"Categoria: {dados['categoria']}")
        print(f"Preço: R${dados['preco']:.2f}")
        print(f"Quantidade: {dados['quantidade']}")

    else:
        print("Produto não encontrado!")
