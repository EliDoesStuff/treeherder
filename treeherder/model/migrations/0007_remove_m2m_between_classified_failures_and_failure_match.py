# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 09:29
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('model', '0006_drop_matcher_fks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classifiedfailure',
            name='failure_lines',
        ),
    ]
