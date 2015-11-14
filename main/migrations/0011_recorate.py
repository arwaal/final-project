# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150913_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField()),
                ('reco', models.ForeignKey(to='main.Recommendation')),
            ],
        ),
    ]
