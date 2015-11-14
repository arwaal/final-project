# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_businesssubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='recomendation',
            field=models.ForeignKey(to='main.Recommendation', null=True),
        ),
    ]
