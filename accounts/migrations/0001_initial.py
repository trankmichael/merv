# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 01:44
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='Required. 100 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=100, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name='last name')),
                ('collaborative', accounts.models.IntegerRangeField(blank=True, null=True)),
                ('strength', accounts.models.IntegerRangeField(blank=True, null=True)),
                ('transportation', accounts.models.IntegerRangeField(blank=True, null=True)),
                ('outdoor', accounts.models.IntegerRangeField(blank=True, null=True)),
                ('language', accounts.models.IntegerRangeField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
            },
        ),
    ]
