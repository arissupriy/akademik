# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-26 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0003_siswa_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='foto',
            field=models.FileField(blank=True, upload_to='/home/aris/PycharmProjects/akademik/assets/upload'),
        ),
    ]
