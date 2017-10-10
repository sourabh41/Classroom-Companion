# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_feedback_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='option_A',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_B',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_C',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_D',
        ),
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='answer',
            field=models.CharField(choices=[('T', 'Yes'), ('F', 'No')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebApp.Course'),
        ),
        migrations.AddField(
            model_name='poll',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='if_no_then',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
