# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0007_auto_20170817_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='comment',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Ralphlaa The Winner Babyy'),
            preserve_default=False,
        ),
    ]
