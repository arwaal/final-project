# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_user', models.NullBooleanField()),
                ('address', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('regular_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
