# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class CadastroConfig(AppConfig):
    name = 'wramais.cadastro'
    verbose_name = "Cadastro de Ramais"

    def ready(self):
        pass
