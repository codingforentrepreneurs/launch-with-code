# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JoinFriends'
        db.create_table(u'joins_joinfriends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Sharer', unique=True, to=orm['joins.Join'])),
            ('emailall', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emailall', to=orm['joins.Join'])),
        ))
        db.send_create_signal(u'joins', ['JoinFriends'])

        # Adding M2M table for field friends on 'JoinFriends'
        m2m_table_name = db.shorten_name(u'joins_joinfriends_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('joinfriends', models.ForeignKey(orm[u'joins.joinfriends'], null=False)),
            ('join', models.ForeignKey(orm[u'joins.join'], null=False))
        ))
        db.create_unique(m2m_table_name, ['joinfriends_id', 'join_id'])


    def backwards(self, orm):
        # Deleting model 'JoinFriends'
        db.delete_table(u'joins_joinfriends')

        # Removing M2M table for field friends on 'JoinFriends'
        db.delete_table(db.shorten_name(u'joins_joinfriends_friends'))


    models = {
        u'joins.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'joins.joinfriends': {
            'Meta': {'object_name': 'JoinFriends'},
            'email': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Sharer'", 'unique': 'True', 'to': u"orm['joins.Join']"}),
            'emailall': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emailall'", 'to': u"orm['joins.Join']"}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Friend'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['joins.Join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['joins']