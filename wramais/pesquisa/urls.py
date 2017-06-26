# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.PesquisaRamaisJsonView),
    url(r'^api/ramais$', views.PesquisaRamaisIntranetView.as_view()),
]