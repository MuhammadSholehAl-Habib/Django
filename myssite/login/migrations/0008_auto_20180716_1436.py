# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 07:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20180716_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geojson',
            name='organization',
        ),
        migrations.DeleteModel(
            name='geojson',
        ),
    ]