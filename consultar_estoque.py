from cadastro_de_produtos import estoque


def consultar_estoque():
    """Mostra todos os produtos cadastrados"""

    print("\n========== ESTOQUE ==========")

    if not estoque:
        print("Estoque vazio.")
        return

    print(f"{'PRODUTO':<15} {'CATEGORIA':<15} {'PREÇO':<10} {'QUANTIDADE':<10}")

    print("-" * 55)

    for produto, dados in estoque.items():

        print(
            f"{produto:<15} "
            f"{dados['categoria']:<15} "
            f"R${dados['preco']:<9.2f} "
            f"{dados['quantidade']:<10}"
        )
