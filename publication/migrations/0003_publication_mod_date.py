# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='mod_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
