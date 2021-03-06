# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-06-17 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proposals", "0027_auto_20200502_0540"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalproposal",
            name="video_url",
            field=models.URLField(
                blank=True,
                default="",
                help_text="Short 1-2 min video describing your talk",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="video_url",
            field=models.URLField(
                blank=True,
                default="",
                help_text="Short 1-2 min video describing your talk",
            ),
        ),
    ]
