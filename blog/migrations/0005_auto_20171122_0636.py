# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171023_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='edit_date',
            field=models.DateField(null=True),
        ),
    ]
