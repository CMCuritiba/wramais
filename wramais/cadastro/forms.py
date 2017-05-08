# -*- coding: utf-8 -*-

from django.forms import ModelForm, CharField, DecimalField, DateField, BooleanField
from django.forms.models import inlineformset_factory
from django.forms import formsets, models
from django.forms.models import modelformset_factory
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Button, HTML, ButtonHolder
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions, AppendedText)
from crispy_forms.bootstrap import StrictButton
from django.conf import settings
from decimal import Decimal
from django import forms

from .models import VSetor, VPessoa, Ramal

from datetime import datetime

class RamalPesquisaForm(forms.Form):

	setor = forms.ModelChoiceField(label='Setor', queryset=VSetor.objects.all().order_by('set_nome'), required=True, empty_label='TODOS OS SETORES')
	pessoa = forms.ModelChoiceField(label='Pessoa', queryset=VPessoa.objects.all().order_by('pes_nome'), required=False, empty_label='GERAL')

	def __init__(self, *args, **kwargs):
		super(RamalPesquisaForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				Div('setor', css_class='col-md-6',),
				Div('pessoa', css_class='col-md-6',),
				css_class='col-md-12 row',
			),
			Div(
				Div(
					StrictButton('Pesquisar', css_class="btn-primary btn", id='btn_search', onclick='pesquisa()'),
					StrictButton('Incluir Ramal', css_class="btn-default btn", id='btn_new', onclick='novo()'),
					css_class='col-xs-12',
				),
				css_class='col-xs-12 row',
			),
		)


class RamalForm(forms.ModelForm):		
	class Meta:
		model = Ramal
		fields = ['setor', 'pessoa', 'numero']

	setor = forms.ModelChoiceField(label='Setor', queryset=VSetor.objects.all().order_by('set_nome'), required=True, empty_label='TODOS OS SETORES')
	pessoa = forms.ModelChoiceField(label='Pessoa', queryset=VPessoa.objects.all().order_by('pes_nome'), required=False, empty_label='GERAL')

	def __init__(self, *args, **kwargs):
		super(RamalForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				Div('setor', css_class='col-md-6',),
				Div('pessoa', css_class='col-md-6',),
				css_class='col-md-12 row',
			),
			Div(
				Div('numero', css_class='col-md-12',),
				css_class='col-md-12 row',
			),
		)