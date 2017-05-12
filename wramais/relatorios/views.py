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

from wramais.cadastro.models import VPessoa, VSetor, Ramal
from wramais.cadastro.util.seguranca.seguranca import RamaisLoginRequired

class RelatorioHierarquizadoView(RamaisLoginRequired, PDFTemplateView):
	template_name = "relatorios/hierarquizado.html"
	lista_ramais = None

	def get_context_data(self, **kwargs):
		context = super(RelatorioHierarquizadoView, self).get_context_data(**kwargs)
		context['title'] = 'Relatório Hierarquizado de Ramais'
		context['pagesize'] = 'A4 portrait'

		#self.lista_ramais = Ramal.objects.order_by('setor__set_id')
		self.lista_ramais = Ramal.objects.all()
		self.lista_ramais = self.lista_ramais.filter(setor__set_ativo=True)
		
		context['lista_ramais'] = self.lista_ramais
		return context

	def get(self, request, *args, **kwargs):
		context = super(PDFTemplateView, self).get_context_data(**kwargs)
		return super(RelatorioHierarquizadoView, self).get(request, *args, **kwargs)	