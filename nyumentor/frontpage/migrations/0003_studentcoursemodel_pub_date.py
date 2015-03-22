# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_auto_20150321_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcoursemodel',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
