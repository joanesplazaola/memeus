# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memea', '0004_auto_20161104_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='memea',
            name='igoData',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='memeiruzkina',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
