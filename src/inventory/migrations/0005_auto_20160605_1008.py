# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-05 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_photo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='contact_detail',
            field=models.CharField(default='', help_text='kontaktne informacie - adresa', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, help_text='emailovy kontakt', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', help_text='telefonny kontakt', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='', help_text='meno zakaznika alebo nazov stola', max_length=60),
        ),
    ]
