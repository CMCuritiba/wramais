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
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from wramais.cadastro.models import VPessoa, Ramal
from .forms import RamalPesquisaForm

#--------------------------------------------------------------------------------------
# View para pesquisa de setores/pessoas/ramais
#--------------------------------------------------------------------------------------
class PesquisaRamaisView(SuccessMessageMixin, FormView):
	template_name = 'pesquisa/index.html'
	form_class = RamalPesquisaForm

	def get(self, request, *args, **kwargs):

		context = self.get_context_data(**kwargs)

		setor = self.request.GET.get('setor','0')
		pessoa = self.request.GET.get('pessoa','0')

		if setor == '':
			setor = '0'
		if pessoa == '':
			pessoa = '0'

		#lista_ramais = Ramal.objects.order_by('setor__set_nome')
		lista_ramais = Ramal.objects.all()
		if (setor != '' and setor != '0'):
			lista_ramais = lista_ramais.filter(setor__set_id=setor)
		if (pessoa != '' and pessoa != '0'):
			lista_ramais = lista_ramais.filter(pessoa__pes_matricula=pessoa)

		data = {'setor': setor, 'pessoa': pessoa}
		form = RamalPesquisaForm(initial=data)

		context['form'] = form
		context['lista_ramais'] = lista_ramais

		return self.render_to_response(context)