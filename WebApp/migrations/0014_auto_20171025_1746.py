# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0013_auto_20171025_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='responses',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='timeout',
            field=models.IntegerField(null=True),
        ),
    ]