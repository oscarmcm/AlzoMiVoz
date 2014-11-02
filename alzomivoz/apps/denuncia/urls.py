# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import DenunciaView
from . import views

urlpatterns = patterns('denuncia.views',
    url(r'^denuncias/$', DenunciaView.as_view(), name="denuncia"),
    url(r'^denunciar/$', 'agregar_denuncia', name='add_denuncia'),
    url(r'^estadisticas/$', 'estadistica', name='panel_estadistica')
    )