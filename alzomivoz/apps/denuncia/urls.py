# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import DenunciaView
from . import views

urlpatterns = patterns('denuncia.views',
    url(r'^denuncias/$', DenunciaView.as_view(), name="denuncia"),
    url(r'^denunciar/$', 'agregar_denuncia', name='add_denuncia'),
    url(r'^estadisticas/$', 'estadistica', name='panel_estadistica'),
    url(r'^mapa/$', 'mapa', name='mapa'),
    
    # api
    url(r'^api/v1/posts/$', 'denuncia_collection'),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', 'denuncia_element')
    )