# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0024_remove_front_users_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
    ]
