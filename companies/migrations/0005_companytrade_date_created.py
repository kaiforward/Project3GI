# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_company_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='companytrade',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
