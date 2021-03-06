# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-18 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guru', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('kd_kelas', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('kelas', models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III')], max_length=1)),
                ('nama_kelas', models.CharField(choices=[('A', 'a'), ('B', 'b'), ('C', 'c')], max_length=1)),
                ('jurusan', models.CharField(choices=[('ipa', 'IPA'), ('ips', 'IPS'), ('bahasa', 'BAHASA')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Mapel',
            fields=[
                ('kd_mapel', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_mapel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pengajar',
            fields=[
                ('kd_ajar', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('kd_guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guru.Guru')),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kelas.Kelas')),
                ('mapel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kelas.Mapel')),
            ],
        ),
    ]
