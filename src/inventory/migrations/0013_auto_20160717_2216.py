# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-17 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20160717_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='blob',
            field=models.FileField(blank=True, upload_to=b'/home/morientes/Work/tp-soft/winecart/src/static/data/'),
        ),
    ]