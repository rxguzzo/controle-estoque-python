"""
Classe responsável pelo gerenciamento do estoque.
"""

from models.produto import Produto
from models.movimentacao import Movimentacao


class Estoque:
    def __init__(self):
        self.produtos = {}
        self.movimentacoes = []

    def cadastrar_produto(self, nome):
        """Cadastra um novo produto no estoque."""
        if nome not in self.produtos:
            self.produtos[nome] = Produto(nome)
            print(f"Produto '{nome}' cadastrado com sucesso!")
        else:
            print("Produto já cadastrado.")

    def entrada_produto(self, nome, quantidade, responsavel):
        """Registra entrada de produtos no estoque."""
        if nome in self.produtos:
            self.produtos[nome].adicionar(quantidade)

            movimentacao = Movimentacao(
                "ENTRADA",
                nome,
                quantidade,
                responsavel
            )

            self.movimentacoes.append(movimentacao)
            print(f"Entrada de {quantidade} unidade(s) realizada com sucesso.")
        else:
            print("Produto não encontrado.")

    def saida_produto(self, nome, quantidade, responsavel):
        """Registra saída de produtos do estoque."""
        if nome in self.produtos:
            if self.produtos[nome].remover(quantidade):

                movimentacao = Movimentacao(
                    "SAÍDA",
                    nome,
                    quantidade,
                    responsavel
                )

                self.movimentacoes.append(movimentacao)
                print(f"Saída de {quantidade} unidade(s) realizada com sucesso.")
            else:
                print("Estoque insuficiente para realizar a saída.")
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        """Lista todos os produtos cadastrados."""
        print("\n===== ESTOQUE ATUAL =====")

        if len(self.produtos) == 0:
            print("Nenhum produto cadastrado.")
            return

        for produto in self.produtos.values():
            print(produto)

    def listar_movimentacoes(self):
        """Lista o histórico de movimentações."""
        print("\n===== HISTÓRICO DE MOVIMENTAÇÕES =====")

        if len(self.movimentacoes) == 0:
            print("Nenhuma movimentação registrada.")
            return

        for movimentacao in self.movimentacoes:
            print(movimentacao)