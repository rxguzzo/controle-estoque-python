"""
Projeto: Controle de Estoque
Disciplina: Engenharia de Software

Autor: Gustavo Guzzo Sanches

Descrição:
Sistema simples para controle de entrada e saída de produtos em estoque.
"""

"""
Sistema simples de controle de estoque.

Funcionalidades:
- Cadastro de produtos
- Entrada de produtos no estoque
- Saída de produtos do estoque
- Validação de quantidade disponível
- Registro de data e responsável pela movimentação
"""

from services.estoque import Estoque


def exibir_menu():
    print("\n" + "=" * 45)
    print("      SISTEMA DE CONTROLE DE ESTOQUE")
    print("=" * 45)
    print("1 - Cadastrar produto")
    print("2 - Registrar entrada")
    print("3 - Registrar saída")
    print("4 - Listar estoque")
    print("5 - Histórico de movimentações")
    print("6 - Sair")
    print("=" * 45)


def ler_quantidade(mensagem):
    """Lê e valida uma quantidade inteira positiva."""
    try:
        quantidade = int(input(mensagem))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return None

        return quantidade

    except ValueError:
        print("Quantidade inválida. Digite apenas números inteiros.")
        return None


def main():
    estoque = Estoque()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            estoque.cadastrar_produto(nome)

        elif opcao == "2":
            nome = input("Produto: ")
            quantidade = ler_quantidade("Quantidade recebida: ")

            if quantidade is not None:
                responsavel = input("Responsável: ")
                estoque.entrada_produto(nome, quantidade, responsavel)

        elif opcao == "3":
            nome = input("Produto: ")
            quantidade = ler_quantidade("Quantidade retirada: ")

            if quantidade is not None:
                responsavel = input("Responsável: ")
                estoque.saida_produto(nome, quantidade, responsavel)

        elif opcao == "4":
            estoque.listar_produtos()

        elif opcao == "5":
            estoque.listar_movimentacoes()

        elif opcao == "6":
            print("\nSistema encerrado com sucesso!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()