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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128, choices=[('MATH', 'Math'), ('ENG', 'English'), ('CS', 'Computer Science')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('coursegrade', models.CharField(max_length=128, choices=[('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('F', 'F')])),
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
    ]
