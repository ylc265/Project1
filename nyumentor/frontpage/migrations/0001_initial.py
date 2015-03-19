# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('course_prefix', models.CharField(max_length=128)),
                ('course_number', models.CharField(max_length=128)),
                ('professor', models.CharField(max_length=128)),
                ('course_name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('prof_slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentCourseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('course_grade', models.CharField(choices=[('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('F', 'F')], max_length=128)),
                ('verified', models.BooleanField(default=False)),
                ('course_model', models.ForeignKey(to='frontpage.CourseModel', null=True)),
                ('course_user', models.ForeignKey(to='frontpage_users.UserProfile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
