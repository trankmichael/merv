# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=30, null=True, verbose_name='task name'),
        ),
    ]
