# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created', '-updated'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blog'},
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name='Body'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
            preserve_default=True,
        ),
    ]
