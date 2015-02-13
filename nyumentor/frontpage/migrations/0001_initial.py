# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(choices=[('MATH', 'Math'), ('ENG', 'English'), ('CS', 'Computer Science')], max_length=128, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('coursenumber', models.CharField(max_length=128)),
                ('professor', models.CharField(max_length=128)),
                ('coursename', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('prof_slug', models.SlugField()),
                ('category', models.ForeignKey(to='frontpage.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='coursemodel',
            unique_together=set([('coursenumber', 'professor')]),
        ),
    ]
