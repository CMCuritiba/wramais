# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#---------------------------------------------------------------------------------------------
# Model para a view V_SETOR
#---------------------------------------------------------------------------------------------
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
	set_ativo = models.BooleanField()
	set_tipo = models.CharField(max_length=1)

	def __unicode__(self):
		return self.set_nome

	def __str__(self):
		return self.set_nome

#---------------------------------------------------------------------------------------------
# Model para a view V_PESSOA
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class VPessoa(models.Model):
	class Meta:
		verbose_name_plural = 'Pessoas'		
		managed = False
		db_table = "v_pessoa"

	pes_matricula = models.IntegerField(primary_key=True)
	pes_nome = models.CharField(max_length=500)
	set_id = models.IntegerField()

	def __unicode__(self):
		return self.pes_nome

	def __str__(self):
		return self.pes_nome

#---------------------------------------------------------------------------------------------
# Model para a tabela RAMAL
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class Ramal(models.Model):	

	setor = models.ForeignKey(VSetor, to_field='set_id', db_constraint=False)
	pessoa = models.ForeignKey(VPessoa, to_field='pes_matricula', null=True, db_constraint=False)
	numero = models.CharField(max_length=200)

	def __unicode__(self):
		return self.setor.set_nome + '-' + self.pessoa.pes_nome

	def __str__(self):
		return self.setor.set_nome + '-' + self.pessoa.pes_nome
