# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-21 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20160718_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='awards',
        ),
        migrations.AddField(
            model_name='product',
            name='awards',
            field=models.ManyToManyField(blank=True, help_text='medaily/ocenenia', to='inventory.Award'),
        ),
        migrations.AlterField(
            model_name='award',
            name='name',
            field=models.CharField(blank=True, help_text='nazov', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='blob',
            field=models.FileField(blank=True, upload_to='image/%Y/%m/%d'),
        ),
    ]
