# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-28 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redistricting', '0005_plansubmission_organization_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='plansubmission',
            name='values_choices',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
