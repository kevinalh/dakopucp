# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_auto_20160611_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='filtro_bool',
            field=models.BooleanField(default=True),
        ),
    ]
