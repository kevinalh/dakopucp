# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0009_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='mina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twitter.Lugar'),
        ),
    ]
