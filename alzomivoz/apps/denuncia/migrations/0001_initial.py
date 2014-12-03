# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Denuncia'
        db.create_table(u'denuncia_denuncia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'denuncia', ['Denuncia'])


    def backwards(self, orm):
        # Deleting model 'Denuncia'
        db.delete_table(u'denuncia_denuncia')


    models = {
        u'denuncia.denuncia': {
            'Meta': {'object_name': 'Denuncia'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['denuncia']