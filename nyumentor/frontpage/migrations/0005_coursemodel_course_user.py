# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage_users', '0003_remove_userprofile_courses'),
        ('frontpage', '0004_remove_coursemodel_course_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='course_user',
            field=models.ForeignKey(to='frontpage_users.UserProfile', default='', null=True),
            preserve_default=False,
        ),
    ]
