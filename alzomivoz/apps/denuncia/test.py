# -*- coding: utf-8 -*-

import unittest

from django.test import Client
from django.test import TestCase

from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse

from .models import Denuncia
setup_test_environment()

client = Client()
response = client.get('/')
response.status_code


def crear_denuncia(titulo, autor, lugar):

    return Denuncia.objects.create(titulo=titulo, autor=autor, lugar=lugar)


class DenunciaViewTests(TestCase):

    def test_denuncia_list_sin_denuncia(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = client.get(reverse('denuncias_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['denuncias'], [])

    def test_con_dos_denuncias(self):
        crear_denuncia(titulo="Denuncia1", autor='Jonathan', lugar='Managua')
        crear_denuncia(titulo="Denuncia2", autor='Oscar', lugar='Esteli')
        response = self.client.get(reverse('denuncias_list'))
        self.assertQuerysetEqual(
            response.context['denuncias'].order_by('titulo'),
            ['<Denuncia: Denuncia1>', '<Denuncia: Denuncia2>']
        )
