# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_store', '0002_auto_20170707_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='skus',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]