# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesssubmission',
            name='image',
            field=models.OneToOneField(to='main.Recommendation'),
        ),
    ]
