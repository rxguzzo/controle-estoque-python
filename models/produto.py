"""
Classe que representa um produto do estoque.
"""


class Produto:
    def __init__(self, nome, quantidade=0):
        self.nome = nome
        self.quantidade = quantidade

    def adicionar(self, quantidade):
        """Adiciona quantidade ao estoque."""
        self.quantidade += quantidade

    def remover(self, quantidade):
        """Remove quantidade do estoque caso haja saldo suficiente."""
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            return True
        return False

    def __str__(self):
        return f"{self.nome} - Estoque: {self.quantidade}"