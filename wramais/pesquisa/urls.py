# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^$', views.PesquisaRamaisView.as_view(template_name='pesquisa/index.html'), name='index')
]