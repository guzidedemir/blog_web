# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Workers',
            field=models.ManyToManyField(blank=True, to='Lab.Worker'),
        ),
    ]
