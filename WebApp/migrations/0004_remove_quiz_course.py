# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_auto_20171003_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='course',
        ),
    ]
