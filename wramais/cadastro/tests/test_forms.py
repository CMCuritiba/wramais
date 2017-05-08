# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from ..models import VSetor, VPessoa, Ramal
from django.db import IntegrityError, DataError
from django.contrib.auth import get_user_model

import os

from ..forms import RamalPesquisaForm

class RamalPesquisaFormTest(TestCase):
	fixtures = ['elotech.json', 'cadastro.json']

	def setUp(self):
		user = get_user_model().objects.create_user('administrador')

	def test_init(self):
		form = RamalPesquisaForm()

	def test_pesquisa_setor(self):
		vsetor = VSetor.objects.get(pk=171)
		form_data = {'setor': '171'}
		form = RamalPesquisaForm(data=form_data)
		self.assertTrue(form.is_valid())
		self.assertEqual(form.cleaned_data['setor'], vsetor)

	def test_pesquisa_setor_pessoa(self):
		vsetor = VSetor.objects.get(pk=171)
		vpessoa = VPessoa.objects.get(pk=2179)
		form_data = {'setor': '171', 'pessoa': '2179'}
		form = RamalPesquisaForm(data=form_data)
		self.assertTrue(form.is_valid())
		self.assertEqual(form.cleaned_data['setor'], vsetor)
		self.assertEqual(form.cleaned_data['pessoa'], vpessoa)