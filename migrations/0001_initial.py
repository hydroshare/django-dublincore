# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualifiedDublinCoreElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.CharField(max_length=255)),
                ('term', models.CharField(max_length=4, choices=[(b'AB', b'Abstract'), (b'BX', b'Box'), (b'BIB', b'BibliographicCitation'), (b'CN', b'Contributor'), (b'CVR', b'Coverage'), (b'CR', b'Creator'), (b'DT', b'Date'), (b'DTS', b'DateSubmitted'), (b'DC', b'DateCreated'), (b'DM', b'DateModified'), (b'DTS', b'DateSubmitted'), (b'DSC', b'Description'), (b'FMT', b'Format'), (b'ID', b'Identifier'), (b'LG', b'Language'), (b'PD', b'Period'), (b'PT', b'Point'), (b'PBL', b'Publisher'), (b'REF', b'Reference'), (b'REL', b'Relation'), (b'RT', b'Rights'), (b'SRC', b'Source'), (b'SUB', b'Subject'), (b'T', b'Title'), (b'TYP', b'Type')])),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['term'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QualifiedDublinCoreElementHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.CharField(max_length=255)),
                ('term', models.CharField(max_length=4, choices=[(b'AB', b'Abstract'), (b'BX', b'Box'), (b'BIB', b'BibliographicCitation'), (b'CN', b'Contributor'), (b'CVR', b'Coverage'), (b'CR', b'Creator'), (b'DT', b'Date'), (b'DTS', b'DateSubmitted'), (b'DC', b'DateCreated'), (b'DM', b'DateModified'), (b'DTS', b'DateSubmitted'), (b'DSC', b'Description'), (b'FMT', b'Format'), (b'ID', b'Identifier'), (b'LG', b'Language'), (b'PD', b'Period'), (b'PT', b'Point'), (b'PBL', b'Publisher'), (b'REF', b'Reference'), (b'REL', b'Relation'), (b'RT', b'Rights'), (b'SRC', b'Source'), (b'SUB', b'Subject'), (b'T', b'Title'), (b'TYP', b'Type')])),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('qdce_id_stored', models.PositiveIntegerField(help_text=b'Stores the id if the QulifiedDublinCoreElement the history points to is deleted.')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('qdce', models.ForeignKey(related_name='history', on_delete=django.db.models.deletion.SET_NULL, to='dublincore.QualifiedDublinCoreElement', null=True)),
            ],
            options={
                'ordering': ['term'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
