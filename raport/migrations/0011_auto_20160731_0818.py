# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-31 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raport', '0010_auto_20160730_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raport',
            name='harian',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='raport',
            name='uas',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='raport',
            name='uts',
            field=models.FloatField(blank=True),
        ),
    ]
