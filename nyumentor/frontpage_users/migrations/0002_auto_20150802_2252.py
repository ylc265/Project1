# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import frontpage_users.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=frontpage_users.models.get_path_name),
            preserve_default=True,
        ),
    ]
