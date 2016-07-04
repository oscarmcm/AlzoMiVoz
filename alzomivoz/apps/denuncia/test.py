# -*- coding: utf-8 -*-

import unittest

from django.test import Client
from django.test import TestCase

from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse

from .models import Denuncia
from .forms import DenunciaForm
setup_test_environment()

client = Client()
response = client.get('/')
response.status_code


def crear_denuncia(titulo, autor, lugar):

    return Denuncia.objects.create(titulo=titulo, autor=autor, lugar=lugar)


class DenunciaModelTest(TestCase):

    def test_string_representation(self):
        comment = Denuncia(titulo="Denuncia Temporal")
        self.assertEqual(str(comment), "Denuncia Temporal")


class DenunciaListViewTests(TestCase):

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


class DenunciaFormTest(TestCase):
    def setUp(self):
        self.denuncia = crear_denuncia(titulo="Denuncia1", autor='Jonathan', lugar='Managua')  # NOQA

    def test_init(self):
        with self.assertRaises(TypeError):
            DenunciaForm(denuncia=self.denuncia)

    def test_valid_data(self):
        form = DenunciaForm({
            'titulo': "Turanga Leela",
            'autor': "leela@example.com",
            'lugar': "Hi there",
        })
        self.assertTrue(form.is_valid())
        den = form.save()
        self.assertEqual(den.titulo, "Turanga Leela")
        self.assertEqual(den.autor, "leela@example.com")
        self.assertEqual(den.lugar, "Hi there")

    def test_blank_data(self):
        form = DenunciaForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'autor': [u'Este campo es obligatorio.'],
            'titulo': [u'Este campo es obligatorio.'],
            'lugar': [u'Este campo es obligatorio.'],
        })
