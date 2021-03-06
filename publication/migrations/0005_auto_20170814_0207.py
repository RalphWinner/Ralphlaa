# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-14 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0004_remove_publication_mod_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='edit',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='user',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
