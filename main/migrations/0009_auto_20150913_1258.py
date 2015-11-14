# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150908_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesssubmission',
            name='image',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='telephone',
        ),
        migrations.AddField(
            model_name='businesssubmission',
            name='recomendation',
            field=models.OneToOneField(null=True, blank=True, to='main.Recommendation'),
        ),
        migrations.AlterField(
            model_name='users',
            name='recomendation',
            field=models.ForeignKey(blank=True, to='main.Recommendation', null=True),
        ),
    ]
