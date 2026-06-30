"""
Classe que representa uma movimentação de estoque.
"""

from datetime import datetime


class Movimentacao:
    def __init__(self, tipo, produto, quantidade, responsavel):
        self.tipo = tipo
        self.produto = produto
        self.quantidade = quantidade
        self.responsavel = responsavel
        self.data = datetime.now()

    def __str__(self):
        return (
            f"[{self.data.strftime('%d/%m/%Y %H:%M:%S')}] "
            f"{self.tipo} | Produto: {self.produto} | "
            f"Qtd: {self.quantidade} | Responsável: {self.responsavel}"
        )