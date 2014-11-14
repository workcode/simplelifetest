# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_seo', '__first__'),
        ('blog', '0003_blog_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMetadata',
            fields=[
                ('allmetadata_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='simple_seo.AllMetadata')),
            ],
            options={
            },
            bases=('simple_seo.allmetadata',),
        ),
    ]
