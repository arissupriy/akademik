# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-19 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raport', '0006_auto_20160719_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raport',
            name='uas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='raport',
            name='uts',
            field=models.FloatField(),
        ),
    ]
