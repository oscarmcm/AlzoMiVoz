# -*- coding: utf-8 -*-
from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import redirect
from django.views.generic import FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q, Count



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from denuncia.serializers import PostSerializer

import json
import time

from .models import Denuncia
from .forms import DenunciaForm

class DenunciaList(ListView):
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

            return HttpResponseRedirect(reverse('denuncias_list'))

    else:
        form = DenunciaForm()

    return render(request, 'denuncia/denuncia_form.html', {'form': form})
          

def estadistica(request, template='denuncia/panel.html'):
    """panel de estadistica para las denuncias"""
    
    return render(request, template, {})

def mapa(request, template='denuncia/mapa.html'):
    """mapa de incidencias"""

    return render(request, template, {})

@api_view(['GET', 'POST'])
def denuncia_collection(request):
    if request.method == 'GET':
        denuncia = Denuncia.objects.all()
        serializer = PostSerializer(denuncia, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'titulo': request.DATA.get('titulo'),'imagen': request.DATA.get('imagen'), 'autor': request.DATA.get('autor')}
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def denuncia_element(request, pk):
    try:
        denuncia = Denuncia.objects.get(pk=pk)
    except Denuncia.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(denuncia)
        return Response(serializer.data)