# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-19 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raport',
            name='id_guru',
        ),
        migrations.RemoveField(
            model_name='raport',
            name='id_kelas',
        ),
        migrations.RemoveField(
            model_name='raport',
            name='id_mapel',
        ),
        migrations.RemoveField(
            model_name='raport',
            name='id_siswa',
        ),
        migrations.DeleteModel(
            name='Raport',
        ),
    ]
