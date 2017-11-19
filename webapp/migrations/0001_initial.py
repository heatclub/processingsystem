# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=20)),
                ('issue_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='sync_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in_seconds', models.IntegerField()),
                ('issue_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=140)),
                ('video_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
