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

from .models import Ramal

from datetime import datetime

class RamalPesquisaForm(forms.Form):
	pass

class RamalForm(forms.ModelForm):
	class Meta:
		model = Ramal
		fields = ['setor', 'numero', 'principal']

	def __init__(self, *args, **kwargs):
		super(RamalForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				Div('setor', css_class='col-md-6',),
				Div('numero', css_class='col-md-6',),
				css_class='col-md-12 row',
			),
			Div(
				Div('principal', css_class='col-md-12',),
				css_class='col-md-12 row',
			),
		)