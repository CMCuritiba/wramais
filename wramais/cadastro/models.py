# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#---------------------------------------------------------------------------------------------
# Model para a tabela RAMAL
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class Ramal(models.Model):	

	setor = models.IntegerField()
	numero = models.CharField(max_length=4)
	principal = models.BooleanField(default=False)

	def __unicode__(self):
		return self.numero

	def __str__(self):
		return self.numero
