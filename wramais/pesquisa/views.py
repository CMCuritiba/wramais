# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
import json
from wramais.cadastro.models import VPessoa, Ramal
from .forms import RamalPesquisaForm
from django.db import connections
from restless.views import Endpoint
from django.shortcuts import render

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

def PesquisaRamaisJsonView(request):
	context = {}
	return render(request,'pesquisa/index2.html',context)


class PesquisaRamaisIntranetView(Endpoint):
    def get(self, request):
        cursor = connections['default'].cursor()
        cursor.execute("select upper(v_setor.set_nome), upper(v_pessoa.pes_nome), numero from cadastro_ramal left join v_pessoa on cadastro_ramal.pessoa_id = v_pessoa.pes_matricula left join v_setor on cadastro_ramal.setor_id = v_setor.set_id order by v_setor.set_nome")
        json_data = json.dumps(cursor.fetchall(), sort_keys=True, indent=4)
        json_data = "{\"data\": " + json_data + "}"
        #print(json_data)
        return HttpResponse(json_data, content_type="application/json")