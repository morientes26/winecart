# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-01 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_auto_20160801_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
