# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 02:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171211_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 12, 2, 21, 7, 862905, tzinfo=utc), null=True),
        ),
    ]
