# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-19 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kelas', '0004_auto_20160719_1228'),
        ('siswa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='kelas_sekarang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kelas.Kelas'),
        ),
    ]