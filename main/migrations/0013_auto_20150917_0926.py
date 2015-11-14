# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150916_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='contact',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='businesssubmission',
            name='contact',
        ),
        migrations.AddField(
            model_name='businesssubmission',
            name='mobile_number',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='businesssubmission',
            name='pending',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='businesssubmission',
            name='phone_number',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='mobile_number',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='phone_number',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
