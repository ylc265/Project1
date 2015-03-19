# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_auto_20150318_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='slug',
            field=models.SlugField(max_length=128),
            preserve_default=True,
        ),
    ]
