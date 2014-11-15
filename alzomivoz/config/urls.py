# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alzomivoz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),   
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^error/', TemplateView.as_view(template_name="error.html")),
    url(r'^denuncia/', include('denuncia.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
) 


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)