# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class PesquisaConfig(AppConfig):
    name = 'wramais.pesquisa'
    verbose_name = "Pesquisa de Ramais"

    def ready(self):
        pass
