# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojosecret', '0005_auto_20170623_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='dojosecret.Author'),
        ),
    ]
