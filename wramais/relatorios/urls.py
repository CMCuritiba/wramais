# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^hierarquizado/$', views.RelatorioHierarquizadoView.as_view(template_name='relatorios/hierarquizado.html'), name='relatorio-hierarquizado'),
]