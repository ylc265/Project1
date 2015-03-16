# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0004_remove_coursemodel_course_user'),
        ('frontpage_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='courses',
            field=models.ManyToManyField(to='frontpage.CourseModel'),
            preserve_default=True,
        ),
    ]
