# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vacancy'
        db.create_table(u'vacancies_vacancy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('career', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('pubDate', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=360, null=True, blank=True)),
        ))
        db.send_create_signal(u'vacancies', ['Vacancy'])


    def backwards(self, orm):
        # Deleting model 'Vacancy'
        db.delete_table(u'vacancies_vacancy')


    models = {
        u'vacancies.vacancy': {
            'Meta': {'object_name': 'Vacancy'},
            'career': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '360', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pubDate': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['vacancies']