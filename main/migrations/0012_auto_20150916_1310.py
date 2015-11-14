# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_recorate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recorate',
            name='reco',
        ),
        migrations.AddField(
            model_name='comment',
            name='recomendation',
            field=models.ForeignKey(default=1, to='main.Recommendation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommendation',
            name='down_votes',
            field=models.ManyToManyField(related_name='down_votes', to='main.Users'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='up_votes',
            field=models.ManyToManyField(related_name='up_votes', to='main.Users'),
        ),
        migrations.DeleteModel(
            name='RecoRate',
        ),
    ]
