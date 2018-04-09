# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.shortcuts import render_to_response
import json
from django.core import serializers
from easy_pdf.views import PDFTemplateView
from django.contrib import messages

from wramais.cadastro.models import Ramal
from wramais.cadastro.util.seguranca.seguranca import RamaisLoginRequired

class RelatorioHierarquizadoView(PDFTemplateView):
	template_name = "relatorios/hierarquizado.html"
	lista_ramais = None
	#pdf_filename = "lista_ramais.pdf"

	def get_context_data(self, **kwargs):
		pass

	def get(self, request, *args, **kwargs):
		pass