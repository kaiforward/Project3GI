# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0015_auto_20171122_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='last_checked',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]