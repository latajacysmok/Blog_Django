# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171211_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]