# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 02:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_auto_20170316_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
    ]
