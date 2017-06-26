# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^$', views.PesquisaRamaisView.as_view(template_name='pesquisa/index2.html'), name='index'),
    url(r'^api/ramais$', views.PesquisaRamaisIntranetView.as_view()),
]