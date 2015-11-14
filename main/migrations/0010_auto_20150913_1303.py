# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150913_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesssubmission',
            name='email',
            field=models.EmailField(unique=True, max_length=250),
        ),
    ]
