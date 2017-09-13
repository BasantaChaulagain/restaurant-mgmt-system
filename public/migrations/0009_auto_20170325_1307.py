# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0008_auto_20170325_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordered_food',
            name='qtt',
        ),
        migrations.AlterField(
            model_name='ordered_food',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordered_food',
            name='table',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='public.Table'),
        ),
    ]