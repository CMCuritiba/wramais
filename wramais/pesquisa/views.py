# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
import json
from wramais.cadastro.models import Ramal
from .forms import RamalPesquisaForm
from django.db import connections
from restless.views import Endpoint
from django.shortcuts import render


def PesquisaRamaisJsonView(request):
	context = {}
	return render(request,'pesquisa/index2.html',context)
