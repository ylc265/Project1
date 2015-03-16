# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0003_coursemodel_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='course_user',
        ),
    ]
