# -*- coding: utf-8 -*-
from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import redirect
from django.views.generic import FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q, Count

import json
import time

from .models import Denuncia
from .forms import DenunciaForm

class DenunciaView(ListView):
    """vista en modo lista para las denuncia"""
    models = Denuncia
    context_object_name = 'denuncias'
    queryset = Denuncia.objects.all()
    template_name = 'denuncia/denuncia_list.html'

def agregar_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            nueva_denuncia = form.save()

            return HttpResponseRedirect(reverse('denuncias:denuncias', args=(nueva_denuncia.pk,)))
    else:
        form = DenunciaForm()

    return render(request, 'denuncia/denuncia_form.html', {'form': form})
          

def estadistica(request, template='denuncia/panel.html'):
    """panel de estadistica para las denuncias"""
    
    return render(request, template, {})
        