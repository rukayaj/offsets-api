# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-13 15:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biodiversityloss',
            old_name='type_of_trigger',
            new_name='type',
        ),
    ]
