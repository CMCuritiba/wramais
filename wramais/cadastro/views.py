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

from .models import VPessoa, Ramal
from .forms import RamalPesquisaForm, RamalForm
from .util.seguranca.seguranca import RamaisLoginRequired

#--------------------------------------------------------------------------------------
# Retorna JSON das pessoas lotadas no setor especificado
#--------------------------------------------------------------------------------------
def pessoa_json(request, id):
	resposta = []

	if id == None or id == '' or id == '0':
		pessoas = VPessoa.objects.all()
	else:
		pessoas = VPessoa.objects.filter(set_id=id)

	for p in pessoas:
		pessoa_json = {}
		pessoa_json['id'] = p.pes_matricula
		pessoa_json['nome'] = p.pes_nome
		resposta.append(pessoa_json)

	
	return JsonResponse(resposta, safe=False)	

#--------------------------------------------------------------------------------------
# View para pesquisa de setores/pessoas/ramais
#--------------------------------------------------------------------------------------
class CadastroRamaisIndexView(RamaisLoginRequired, SuccessMessageMixin, FormView):
	template_name = 'cadastro/index.html'
	form_class = RamalPesquisaForm

	def get(self, request, *args, **kwargs):

		context = self.get_context_data(**kwargs)

		setor = self.request.GET.get('setor','0')
		pessoa = self.request.GET.get('pessoa','0')

		if setor == '':
			setor = '0'
		if pessoa == '':
			pessoa = '0'

		lista_ramais = Ramal.objects.order_by('setor__set_nome')
		if (setor != '' and setor != '0'):
			lista_ramais = lista_ramais.filter(setor__set_id=setor)
		if (pessoa != '' and pessoa != '0'):
			lista_ramais = lista_ramais.filter(pessoa__pes_matricula=pessoa)

		data = {'setor': setor, 'pessoa': pessoa}
		form = RamalPesquisaForm(initial=data)

		context['form'] = form
		context['lista_ramais'] = lista_ramais

		return self.render_to_response(context)

#--------------------------------------------------------------------------------------
# View para inclusão de ramais
#--------------------------------------------------------------------------------------
class CadastroRamaisCreateView(RamaisLoginRequired, SuccessMessageMixin, CreateView):
	template_name = "cadastro/new.html"
	form_class = RamalForm
	model = Ramal
	success_url = '/cadastro/'
	success_message = "Ramal criado com sucesso"

#--------------------------------------------------------------------------------------
# View para alteração de ramais
#--------------------------------------------------------------------------------------
class CadastroRamaisUpdateView(RamaisLoginRequired, SuccessMessageMixin, UpdateView):
	template_name = "cadastro/update.html"
	form_class = RamalForm
	model = Ramal
	success_url = '/cadastro/'
	success_message = "Ramal alterado com sucesso"			

#--------------------------------------------------------------------------------------
# View para exclusão de ramais
#--------------------------------------------------------------------------------------
class CadastroRamaisDeleteView(RamaisLoginRequired, SuccessMessageMixin, DeleteView):
	model = Ramal
	success_url = '/cadastro/'
	success_message = "Ramal excluído com sucesso."

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(CadastroRamaisDeleteView, self).delete(request, *args, **kwargs)
