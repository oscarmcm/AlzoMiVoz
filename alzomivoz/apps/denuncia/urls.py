# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import DenunciaList

urlpatterns = patterns('denuncia.views',
    url(r'^listar/$', DenunciaList.as_view(), name="denuncias_list"),
    url(r'^agregar/$', 'agregar_denuncia', name='agregar_denuncia'),
    url(r'^estadisticas/$', 'estadistica', name='panel_estadistica'),
    url(r'^mapa/$', 'mapa', name='mapa'),

    # api
    url(r'^api/v1/posts/$', 'denuncia_collection'),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', 'denuncia_element')
    )