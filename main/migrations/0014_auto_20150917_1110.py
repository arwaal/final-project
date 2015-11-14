# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150917_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businesssubmission',
            old_name='mobile_number',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='businesssubmission',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='email',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='facebook',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='instagram',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='twitter',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='website',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='youtube',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
