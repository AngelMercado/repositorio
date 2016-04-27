# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.pub_date'
        db.add_column(u'events_event', 'pub_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2016, 2, 21, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.pub_date'
        db.delete_column(u'events_event', 'pub_date')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '180', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['events']