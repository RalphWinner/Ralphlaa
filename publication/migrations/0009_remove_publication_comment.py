# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0008_publication_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='comment',
        ),
    ]