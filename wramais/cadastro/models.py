# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class VSetor(models.Model):
	class Meta:
		verbose_name_plural = 'Setores'
		managed = False
		db_table = "v_setor"

	set_id = models.IntegerField(primary_key=True)
	set_nome = models.CharField(max_length=500)
	set_sigla = models.CharField(max_length=100)
	set_id_superior = models.IntegerField(blank=True, null=True)
	etr_id = models.IntegerField()
	set_ativo = models.IntegerField()

@python_2_unicode_compatible
class VPessoa(models.Model):
	class Meta:
		verbose_name_plural = 'Pessoas'		
		managed = False
		db_table = "v_pessoa"

	pes_matricula = models.IntegerField(primary_key=True)
	pes_nome = models.CharField(max_length=500)
	set_id = models.IntegerField()