# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=30)),
                ('es_hashtag', models.BooleanField()),
                ('es_nombre', models.BooleanField()),
            ],
        ),
    ]
