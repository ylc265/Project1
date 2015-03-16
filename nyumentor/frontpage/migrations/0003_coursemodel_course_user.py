# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage_users', '0001_initial'),
        ('frontpage', '0002_auto_20150214_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='course_user',
            field=models.ManyToManyField(to='frontpage_users.UserProfile'),
            preserve_default=True,
        ),
    ]
