# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-10-12 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0002_gig'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slogan',
            field=models.CharField(default='My slogan', max_length=1000),
            preserve_default=False,
        ),
    ]
