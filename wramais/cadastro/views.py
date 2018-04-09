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

from .models import Ramal
from .forms import RamalPesquisaForm, RamalForm
from .util.seguranca.seguranca import RamaisLoginRequired

#--------------------------------------------------------------------------------------
# View para pesquisa de setores/pessoas/ramais
#--------------------------------------------------------------------------------------
class CadastroRamaisIndexView(SuccessMessageMixin, FormView):
	template_name = 'cadastro/index.html'
	form_class = RamalPesquisaForm

	def get(self, request, *args, **kwargs):
		pass

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
