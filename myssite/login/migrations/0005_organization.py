# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_siapsat'),
    ]

    operations = [
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('priority_type', models.CharField(max_length=20)),
                ('combat_type', models.CharField(max_length=20)),
                ('is_induk', models.BooleanField()),
                ('is_rahwan', models.BooleanField()),
                ('parent_id', models.IntegerField()),
                ('level_0_id', models.IntegerField()),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('img_path', models.CharField(max_length=100)),
                ('leader', models.CharField(max_length=50)),
                ('vice_leader', models.CharField(max_length=50)),
            ],
        ),
    ]