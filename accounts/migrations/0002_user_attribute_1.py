# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='attribute_1',
            field=models.CharField(max_length=30, null=True, verbose_name='attribute 1'),
        ),
    ]
