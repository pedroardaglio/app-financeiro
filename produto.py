#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import Decimal


class Produto:
    """."""

    def __init__(self, nome=None, preco_vista=None, preco_parcela=None,
                 qtde_parcelas=None):
        """Construtor."""
        self._nome = nome
        self._preco_vista = Decimal(preco_vista)
        self._preco_parcela = Decimal(preco_parcela)
        self._qtde_parcelas = qtde_parcelas

    def get_nome(self):
        """Obtem o atributo nome."""
        return self._nome

    def get_preco_vista(self):
        """Obtem o atributo preco_vista."""
        return self._preco_vista

    def get_preco_parcela(self):
        """Obtem o atributo preco_parcela."""
        return self._preco_parcela

    def get_qtde_parcelas(self):
        """Obtem o atributo qtde_parcelas."""
        return self._qtde_parcelas

    def set_nome(self, nome):
        """Setta o atributo nome."""
        self._nome = nome

    def set_preco_vista(self, preco_vista):
        """Setta o atributo preco_vista."""
        self._preco_vista = Decimal(preco_vista)

    def set_preco_parcela(self, preco_parcela):
        """Setta o atributo preco_parcela."""
        self._preco_parcela = Decimal(preco_parcela)

    def set_qtde_parcelas(self, qtde_parcelas):
        """Setta o atributo qtde_parcelas."""
        self._qtde_parcelas = qtde_parcelas

    def valor_total_prazo(self):
        """Retorna o valor total do produto a prazo."""
        if self._qtde_parcelas and self._preco_parcela:
            return Decimal(self._qtde_parcelas) * self._preco_parcela

        return None

    def porcentagem_juros(self):
        """Define a porcentagem de juros do valor total."""
        _total_prazo = self.valor_total_prazo()

        if not _total_prazo:
            return None

        n = (_total_prazo - self.get_preco_vista()) * Decimal('100')
        d = self.get_preco_vista()

        r = n / d  # 35

        r2 = str(r).split(".")[0]
        r3 = "0." + r2

        return Decimal(r3)

    def valor_juros_parcela(self):
        """Retorna o valor, em reais, de juros de uma parcela."""
        _preco_parcela_vista = \
            self.get_preco_vista() / Decimal(self.get_qtde_parcelas)

        return self.get_preco_parcela - _preco_parcela_vista

    def valor_juros_total(self):
        """Retorna o valor, em reais, so do juros."""
        return self.valor_total_prazo - self.get_preco_vista()
