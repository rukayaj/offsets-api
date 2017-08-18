# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 09:22
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170714_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='development',
            name='footprint',
            field=django.contrib.gis.db.models.fields.PolygonField(help_text='Should be a .geojson file.', srid=4326),
        ),
        migrations.AlterField(
            model_name='development',
            name='permits',
            field=models.ManyToManyField(help_text='May be one of several, linked to the Permit model.', to='core.Permit'),
        ),
        migrations.AlterField(
            model_name='development',
            name='type',
            field=models.CharField(choices=[('AG', 'Agriculture'), ('BU', 'Business'), ('GO', 'Government'), ('GP', 'Government purposes'), ('IN', 'Industrial'), ('MI', 'Mining'), ('MU', 'Multi-use (public, residential, commercial)'), ('RC', 'Recreational'), ('RE', 'Residential'), ('TR', 'Transport'), ('UN', 'Unknown')], help_text='Choose the one which fits best.', max_length=2),
        ),
        migrations.AlterField(
            model_name='development',
            name='year',
            field=models.IntegerField(help_text='The year in which the development was completed.'),
        ),
    ]