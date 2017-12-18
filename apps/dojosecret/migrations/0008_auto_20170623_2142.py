# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojosecret', '0007_auto_20170623_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='dojosecret.Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='book_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='dojosecret.Book'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='dojosecret.User'),
            preserve_default=False,
        ),
    ]
