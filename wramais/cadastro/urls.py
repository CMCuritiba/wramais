# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^api/pessoas/(?P<id>[0-9]+)/$', views.pessoa_json, name='api-pessoas'),
	url(r'^$', views.CadastroRamaisIndexView.as_view(template_name='cadastro/index.html'), name='index'),
	url(r'^novo/$', views.CadastroRamaisCreateView.as_view(template_name='cadastro/new.html'), name='ramal-novo'),
	url(r'^altera/(?P<pk>[0-9]+)/$', views.CadastroRamaisUpdateView.as_view(template_name='cadastro/update.html'), name='ramal-altera'),
	url(r'^exclui/(?P<pk>[0-9]+)/$', views.CadastroRamaisDeleteView.as_view(), name='ramal-exclui'),
]