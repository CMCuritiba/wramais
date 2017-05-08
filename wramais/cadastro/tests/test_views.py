# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory, Client
from unittest.mock import patch, MagicMock, Mock

class CadastroViewTests(TestCase):
	fixtures = ['elotech.json', 'cadastro.json']

	def test_index(self):
		response = self.client.get('/cadastro/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('lista_ramais' in response.context)

	def test_index_pesquisa_setor(self):
		response = self.client.get('/cadastro/', {'setor': '171'})
		self.assertEqual(response.status_code, 200)
		self.assertTrue('lista_ramais' in response.context)

	def test_index_pesquisa_setor_pessoa(self):
		response = self.client.get('/cadastro/', {'setor': '171', 'pessoa': '2179'})
		self.assertEqual(response.status_code, 200)
		self.assertTrue('lista_ramais' in response.context)