# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-12 13:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171122_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default='', max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2017, 12, 12, 14, 4, 10, 96687))),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='together',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Question'),
        ),
    ]
