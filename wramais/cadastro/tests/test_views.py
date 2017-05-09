# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory, Client
from unittest.mock import patch, MagicMock, Mock
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from ..views import CadastroRamaisCreateView, CadastroRamaisUpdateView, CadastroRamaisDeleteView

class CadastroViewTests(TestCase):
	fixtures = ['elotech.json', 'cadastro.json']

	def setUp(self):
		user = get_user_model().objects.create_user('zaca', password='zaca')
		user.is_staff = True
		user.is_superuser = True
		user.save()

	def test_index(self):
		self.client.login(username='zaca', password='zaca')
		response = self.client.get('/cadastro/', follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('lista_ramais' in response.context)

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

class CadastroCreateViewTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user('zaca', password='zaca')
		self.user.is_staff = True
		self.user.is_superuser = True
		self.user.save()
		self.factory = RequestFactory()

	def test_url(self):
		request = self.factory.get('/cadastro/novo/')
		request.user = self.user
		response = CadastroRamaisCreateView.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Alexandre Odoni')
'''
class CadastroUpdateViewTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user('zaca', password='zaca')
		self.user.is_staff = True
		self.user.is_superuser = True
		self.user.save()
		self.factory = RequestFactory()

	def test_url(self):
		request = self.factory.get('/cadastro/altera/1')
		request.user = self.user
		response = CadastroRamaisUpdateView.as_view()(request)
		#response.render()
		self.assertEqual(response.status_code, 200)

class CadastroDeleteViewTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user('zaca', password='zaca')
		self.user.is_staff = True
		self.user.is_superuser = True
		self.user.save()
		self.factory = RequestFactory()

	def test_url(self):
		request = self.factory.get('/cadastro/exclui/1')
		request.user = self.user
		response = CadastroRamaisDeleteView.as_view()(request)
		#response.render()
		self.assertEqual(response.status_code, 200)
'''		