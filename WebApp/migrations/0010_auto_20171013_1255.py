# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0009_auto_20171004_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='response',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='feedback',
            name='responses',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='responses',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
