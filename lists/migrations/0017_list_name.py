# Generated by Django 2.1.4 on 2018-12-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0016_auto_20181224_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
