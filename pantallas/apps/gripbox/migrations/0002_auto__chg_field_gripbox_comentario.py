# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GripBox.comentario'
        db.alter_column(u'gripbox_gripbox', 'comentario', self.gf('django.db.models.fields.TextField')(max_length=500, null=True))

    def backwards(self, orm):

        # Changing field 'GripBox.comentario'
        db.alter_column(u'gripbox_gripbox', 'comentario', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    models = {
        u'gripbox.gripbox': {
            'Meta': {'object_name': 'GripBox'},
            'comentario': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gripbox']