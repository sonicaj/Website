# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0025_roles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roles',
            name='id',
        ),
        migrations.AlterField(
            model_name='roles',
            name='role_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
