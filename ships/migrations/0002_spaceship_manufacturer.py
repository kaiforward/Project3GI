# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaceship',
            name='manufacturer',
            field=models.CharField(choices=[('CL', 'Clarke Labs'), ('ZS', "Zorg's Shipyard"), ('F', 'Foundation')], default='CL', max_length=50),
        ),
    ]
