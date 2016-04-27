# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'home_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('docfile', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length='200', null=True, blank=True)),
        ))
        db.send_create_signal(u'home', ['Slide'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table(u'home_slide')


    models = {
        u'home.slide': {
            'Meta': {'object_name': 'Slide'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['home']