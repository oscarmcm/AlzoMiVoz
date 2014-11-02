# -*- coding: utf-8 -*-
from django.db import models

class Denuncia(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='denuncia/', blank=True, null=True)
    autor = models.CharField(max_length=60)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Denuncia"
        verbose_name_plural = "Denuncias"