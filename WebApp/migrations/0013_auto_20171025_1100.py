# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0012_question_correct_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='Feedback',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True),
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
