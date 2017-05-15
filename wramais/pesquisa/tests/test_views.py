# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory, Client
from unittest.mock import patch, MagicMock, Mock
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from wramais.cadastro.models import VSetor, VPessoa, Ramal
from ..views import PesquisaRamaisView

class RelatorioHierarquizadoViewTests(TestCase):
	fixtures = ['elotech.json', 'cadastro.json']

	def setUp(self):
		self.user = get_user_model().objects.create_user('zaca', password='zaca')
		self.user.is_staff = True
		self.user.is_superuser = True
		self.user.save()
		self.factory = RequestFactory()

	def setup_request(self, request):
		request.user = self.user

		middleware = SessionMiddleware()
		middleware.process_request(request)
		request.session.save()

		middleware = MessageMiddleware()
		middleware.process_request(request)
		request.session.save()

		request.session['some'] = 'some'
		request.session.save()

	def test_index(self):
		request = self.factory.get('/cadastro/')
		self.setup_request(request)
		request.user = self.user
		response = PesquisaRamaisView.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.template_name[0], 'pesquisa/index.html')

'''
	def test_relatorio(self):
		request = self.factory.get('/relatorios/hierarquizado/')
		self.setup_request(request)
		request.user = self.user
		response = RelatorioHierarquizadoView.as_view()(request)
		self.assertEqual(response.status_code, 200)







	def test_index_pesquisa_setor(self):
		self.client.login(username='zaca', password='zaca')
		response = self.client.get('/cadastro/', {'setor': '171'})
		self.assertEqual(response.status_code, 200)
		self.assertTrue('lista_ramais' in response.context)

	def test_index_pesquisa_setor_pessoa(self):
		self.client.login(username='zaca', password='zaca')
		response = self.client.get('/cadastro/', {'setor': '171', 'pessoa': '2179'})
		self.assertEqual(response.status_code, 200)
		self.assertTrue('lista_ramais' in response.context)
'''		