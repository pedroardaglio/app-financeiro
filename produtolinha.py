#!/usr/bin/env python
# -*- coding: utf-8 -*-
from produto import Produto


class ProdutoLinha(Produto):
    """."""

    def __init__(self, nome=None, preco_vista=None, preco_parcela=None,
                 qtde_parcelas=None, vista_prazo=1):
        """Construtor.

        Igual a classe filha, temos o metodo se e' a vista ou a prazo."""
        self._vista_prazo = vista_prazo
        super()