# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory, Client
from unittest.mock import patch, MagicMock, Mock
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from ..views import CadastroRamaisCreateView, CadastroRamaisUpdateView, CadastroRamaisDeleteView
from ..models import VSetor, VPessoa, Ramal

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

	def test_url(self):
		request = self.factory.get('/cadastro/novo/')
		request.user = self.user
		response = CadastroRamaisCreateView.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Alexandre Odoni')

	def test_salva_ramal_ok(self):
		total_ramais = Ramal.objects.count()
		form_data = {
			'setor': '171',
			'pessoa': '2179',
			'numero': '1234'
		}
		request = self.factory.post('/cadastro/novo/', data=form_data)
		self.setup_request(request)
		request.user = self.user
		response = CadastroRamaisCreateView.as_view()(request)
		self.failUnlessEqual(response.status_code, 302)
		self.assertEqual(Ramal.objects.count(), total_ramais+1)

	def test_salva_ramal_numero_nulo(self):
		total_ramais = Ramal.objects.count()
		data = {
			'setor': '171',
			'pessoa': '2179'
		}
		request = self.factory.post('/cadastro/novo/', data)
		self.setup_request(request)
		request.user = self.user
		response = CadastroRamaisCreateView.as_view()(request)
		self.assertEqual(Ramal.objects.count(), total_ramais)
		self.failUnlessEqual(response.status_code, 200)


class CadastroUpdateViewTests(TestCase):
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

	def test_get(self):
		request = self.factory.get('/cadastro/altera/')
		self.setup_request(request)
		request.user = self.user
		response = CadastroRamaisUpdateView.as_view()(request, pk=1)
		response.render()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.template_name[0], 'cadastro/update.html')

	def test_post_ok(self):
		total_ramais = Ramal.objects.count()
		form_data = {
			'setor': '171',
			'pessoa': '2179',
			'numero': '2579'
		}
		request = self.factory.post('/cadastro/altera/', data=form_data)
		self.setup_request(request)
		request.user = self.user
		response = CadastroRamaisUpdateView.as_view()(request, pk=1)
		self.failUnlessEqual(response.status_code, 302)
		self.assertEqual(Ramal.objects.count(), total_ramais)

	def test_post_erro(self):
		total_ramais = Ramal.objects.count()
		form_data = {
			'setor': '171',
			'pessoa': '2179'
		}
		request = self.factory.post('/cadastro/altera/', data=form_data)
		self.setup_request(request)
		request.user = self.user
		response = CadastroRamaisUpdateView.as_view()(request, pk=1)
		self.failUnlessEqual(response.status_code, 200)


class CadastroDeleteViewTests(TestCase):
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

	def test_post_ok(self):
		total_ramais = Ramal.objects.count()
		request = self.factory.post('/cadastro/exclui/')
		self.setup_request(request)
		request.user = self.user
		response = CadastroRamaisDeleteView.as_view()(request, pk=1)
		self.failUnlessEqual(response.status_code, 302)
		self.assertEqual(Ramal.objects.count(), total_ramais-1)