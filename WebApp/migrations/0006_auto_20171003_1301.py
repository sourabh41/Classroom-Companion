# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_quiz_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_A',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_B',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_C',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_D',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
