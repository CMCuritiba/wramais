# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from ..models import VSetor, VPessoa, Ramal, RamalEspecial
from django.db import IntegrityError, DataError
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


class CadastroTestCase(TestCase):
	fixtures = ['elotech.json', 'cadastro.json']

	def setUp(self):
		super(CadastroTestCase, self).setUp()

	def test_dummy(self):
		self.assertEqual(1, 1)

	def test_ramal_setor_pessoa(self):
		vsetor = VSetor.objects.get(pk=171)
		vpessoa = VPessoa.objects.get(pk=2179)
		ramal = Ramal.objects.create(setor=vsetor, pessoa=vpessoa, numero='1234')
		self.assertEqual(ramal.pessoa.pk, 2179)

	def test_ramal_setor(self):
		vsetor = VSetor.objects.get(pk=171)
		ramal = Ramal.objects.create(setor=vsetor, numero='1234')
		self.assertEqual(ramal.setor.pk, 171)

	def test_ramal_setor_erro(self):
		with self.assertRaises(IntegrityError):
			ramal = Ramal.objects.create(numero='1234')

	def test_ramal_vazio(self):
		vsetor = VSetor.objects.get(pk=171)
		with self.assertRaises(IntegrityError):
			ramal = Ramal.objects.create(setor=vsetor, numero=None)

class RamalEspecialTestCase(TestCase):
	fixtures = ['ramal_especial.json']

	def setUp(self):
		super(RamalEspecialTestCase, self).setUp()

	def test_dummy(self):
		self.assertEqual(1, 1)

	def test_ramal_especial_insere_ok(self):
		ramal_especial = RamalEspecial.objects.create(setor='Caixa Econômica Federal', pessoa='Zaca Zacariano', numero='4444-3333')
		self.assertEqual(ramal_especial.pessoa, 'Zaca Zacariano')

	def test_ramal_especial_setor_erro(self):
		with self.assertRaises(IntegrityError):
			ramal_especial = RamalEspecial.objects.create(setor=None, pessoa='Zaca Zacariano', numero='1234')

	def test_ramal_especial_pessoa_erro(self):
		with self.assertRaises(IntegrityError):
			ramal_especial = RamalEspecial.objects.create(setor='Caixa Econômica Federal', pessoa=None, numero='1234')

	def test_ramal_especial_numero_erro(self):
		with self.assertRaises(IntegrityError):
			ramal_especial = RamalEspecial.objects.create(setor='Caixa Econômica Federal', pessoa='Zaca Zacariano', numero=None)