# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory, Client
from unittest.mock import patch, MagicMock, Mock
from django.contrib.auth import get_user_model
import json
import codecs

class ApiPessoaTest(TestCase):
	fixtures = ['elotech.json', 'cadastro.json']

	def setUp(self):
		pass

	def test_filtro_setor_171(self):
		client = Client()
		response = client.get('/cadastro/api/pessoas/171', follow=True)

		json_decoded = json.loads(response.content.decode('utf-8'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(json_decoded[0]['id'], 2179)

	def test_sem_filtro_setor(self):
		client = Client()
		response = client.get('/cadastro/api/pessoas/0', follow=True)

		json_decoded = json.loads(response.content.decode('utf-8'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(json_decoded), 3)

