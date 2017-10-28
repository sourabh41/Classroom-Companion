# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0015_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='branch',
            field=models.CharField(choices=[('CS', 'Computer Science and Engineering'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('MM', 'Metallurgical Engineering'), ('AE', 'Aerospace Engineering'), ('CE', 'Civil Engineering'), ('CH', 'Chemical Engineering')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('CS', 'Computer Science and Engineering'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('MM', 'Metallurgical Engineering'), ('AE', 'Aerospace Engineering'), ('CE', 'Civil Engineering'), ('CH', 'Chemical Engineering')], max_length=2, null=True),
        ),
    ]