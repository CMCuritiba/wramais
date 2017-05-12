from mimetypes import guess_type

from django import template
from base64 import b64encode
from django.contrib.staticfiles import finders
from django.utils.html import format_html

import os


register = template.Library()

@register.filter
def formata_setor(setor):

    if "DIRETORIA" in setor.upper():
        return format_html("<h2>" + setor + "</h2>")
    if "DEPARTAMENTO" in setor.upper():
        return format_html("<h2>" + setor + "</h2>")
    if "CONTROLADORIA" in setor.upper():
        return format_html("<h2>" + setor + "</h2>")
    if "SETOR" in setor.upper():
        return format_html("<h3 style='margin-left:15px;'>" + setor + "</h3>")
    if "DIVISÃO" in setor.upper():
        return format_html("<h3 style='margin-left:30px;'>" + setor + "</h3>")
    if "SEÇÃO" in setor.upper():
        return format_html("<h3 style='margin-left:20px;'>" + setor + "</h3>")
    return setor

@register.filter
def formata_pessoa(pessoa):
	if pessoa == '' or pessoa is None:
		return 'GERAL'
	return pessoa

@register.filter
def retira_fg(pessoa):
	pessoa = pessoa.replace("Fg-1", "")
	pessoa = pessoa.replace("Fg-2", "")
	pessoa = pessoa.replace("Fg-3", "")
	pessoa = pessoa.replace("Fg-4", "")
	pessoa = pessoa.replace("Fg-5", "")
	pessoa = pessoa.replace("Fg-6", "")
	pessoa = pessoa.replace("Fg-7", "")
	pessoa = pessoa.replace("Fg-8", "")
	return pessoa