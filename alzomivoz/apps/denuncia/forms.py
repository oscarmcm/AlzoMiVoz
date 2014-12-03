# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Denuncia


class DenunciaForm(ModelForm):
	
	class Meta:
		model = Denuncia