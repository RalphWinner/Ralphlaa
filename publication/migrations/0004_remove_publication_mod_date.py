# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0003_publication_mod_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='mod_date',
        ),
    ]