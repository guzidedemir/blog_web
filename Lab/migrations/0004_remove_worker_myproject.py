# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0003_auto_20181108_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='MyProject',
        ),
    ]
