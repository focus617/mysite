# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_list_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
