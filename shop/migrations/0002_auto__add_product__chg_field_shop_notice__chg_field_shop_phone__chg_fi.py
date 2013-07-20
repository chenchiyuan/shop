# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'shop_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Shop'])),
            ('keywords', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal(u'shop', ['Product'])


        # Changing field 'Shop.notice'
        db.alter_column(u'shop_shop', 'notice', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True))

        # Changing field 'Shop.phone'
        db.alter_column(u'shop_shop', 'phone', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Shop.address'
        db.alter_column(u'shop_shop', 'address', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Shop.owner'
        db.alter_column(u'shop_shop', 'owner', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'shop_product')


        # User chose to not deal with backwards NULL issues for 'Shop.notice'
        raise RuntimeError("Cannot reverse this migration. 'Shop.notice' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Shop.phone'
        raise RuntimeError("Cannot reverse this migration. 'Shop.phone' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Shop.address'
        raise RuntimeError("Cannot reverse this migration. 'Shop.address' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Shop.owner'
        raise RuntimeError("Cannot reverse this migration. 'Shop.owner' and its values cannot be restored.")

    models = {
        u'shop.category': {
            'Meta': {'ordering': "[u'region', u'-priority']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Region']"})
        },
        u'shop.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Shop']"}),
            'unit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'shop.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'shop.shop': {
            'Meta': {'object_name': 'Shop'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Category']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'notice': ('django.db.models.fields.TextField', [], {'default': "u''", 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Region']"})
        }
    }

    complete_apps = ['shop']