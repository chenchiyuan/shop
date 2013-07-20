# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'shop_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'shop', ['Region'])

        # Adding model 'Category'
        db.create_table(u'shop_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Region'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'shop', ['Category'])

        # Adding model 'Shop'
        db.create_table(u'shop_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('notice', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Region'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Category'], null=True, blank=True)),
        ))
        db.send_create_signal(u'shop', ['Shop'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'shop_region')

        # Deleting model 'Category'
        db.delete_table(u'shop_category')

        # Deleting model 'Shop'
        db.delete_table(u'shop_shop')


    models = {
        u'shop.category': {
            'Meta': {'ordering': "[u'-priority']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Region']"})
        },
        u'shop.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'shop.shop': {
            'Meta': {'object_name': 'Shop'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Category']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'notice': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Region']"})
        }
    }

    complete_apps = ['shop']