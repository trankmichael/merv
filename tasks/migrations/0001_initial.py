# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.FloatField()),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('task_name', models.CharField(max_length=30, null=True, verbose_name='task name')),
                ('collaborative', tasks.models.IntegerRangeField(blank=True, null=True)),
                ('strength', tasks.models.IntegerRangeField(blank=True, null=True)),
                ('transportation', tasks.models.IntegerRangeField(blank=True, null=True)),
                ('outdoor', tasks.models.IntegerRangeField(blank=True, null=True)),
                ('language', tasks.models.IntegerRangeField(blank=True, null=True)),
            ],
        ),
    ]
