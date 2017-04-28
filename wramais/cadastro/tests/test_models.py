# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from ..models import VSetor, VPessoa
import os

class ElotechViewsTestCase(TestCase):
	fixtures = ['elotech.json']

	def setUp(self):
		super(ElotechViewsTestCase, self).setUp()

	def test_v_setor_ok(self):
		vsetor = VSetor.objects.get(pk=171)
		self.assertEqual(vsetor.set_nome, 'Divisão de Desenvolvimento De Sistemas')

	def test_view_v_pessoa_ok(self):
		vpessoa = VPessoa.objects.get(pk=2179)
		self.assertEqual(vpessoa.pes_nome, 'Alexandre Odoni')