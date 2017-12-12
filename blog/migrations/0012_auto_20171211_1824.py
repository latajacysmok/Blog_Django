# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 02:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20171211_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
