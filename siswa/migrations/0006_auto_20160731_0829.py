# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-31 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0005_auto_20160726_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='foto',
            field=models.ImageField(blank=True, upload_to='/home/aris/PycharmProjects/akademik/assets/upload/siswa'),
        ),
    ]
