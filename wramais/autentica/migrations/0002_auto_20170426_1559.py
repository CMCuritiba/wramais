# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chefia',
            field=models.NullBooleanField(),
        ),
    ]
