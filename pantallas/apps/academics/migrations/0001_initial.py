# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Teacher'
        db.create_table(u'academics_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fullName', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('academy', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'academics', ['Teacher'])


    def backwards(self, orm):
        # Deleting model 'Teacher'
        db.delete_table(u'academics_teacher')


    models = {
        u'academics.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'academy': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'fullName': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['academics']