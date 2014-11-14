# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autocomplete_modified.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('blog', '0002_auto_20141113_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit_autocomplete_modified.managers.TaggableManagerAutocomplete(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
