# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortune',
            name='text',
            field=models.CharField(max_length=2046),
        ),
        migrations.AlterUniqueTogether(
            name='fortune',
            unique_together=set([('pack', 'text')]),
        ),
    ]
