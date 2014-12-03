# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Denuncia.lugar'
        db.add_column(u'denuncia_denuncia', 'lugar',
                      self.gf('django.db.models.fields.CharField')(default='villa nicaragua', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Denuncia.lugar'
        db.delete_column(u'denuncia_denuncia', 'lugar')


    models = {
        u'denuncia.denuncia': {
            'Meta': {'object_name': 'Denuncia'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'fecha_agregado': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['denuncia']