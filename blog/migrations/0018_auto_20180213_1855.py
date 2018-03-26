# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-13 18:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0017_like'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('post', 'user')]),
        ),
    ]