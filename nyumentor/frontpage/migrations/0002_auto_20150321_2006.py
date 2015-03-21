# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcoursemodel',
            name='semester',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Winter', 'Winter')], default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentcoursemodel',
            name='year',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=True,
        ),
    ]
