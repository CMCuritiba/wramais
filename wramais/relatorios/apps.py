# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class RelatoriosConfig(AppConfig):
    name = 'wramais.relatorios'
    verbose_name = "Relatórios dos Ramais"

    def ready(self):
        pass
