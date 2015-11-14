# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150907_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('info', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='recommendation',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image1',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image10',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image2',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image3',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image4',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image5',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image6',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image7',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image8',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image9',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='map_img',
            field=models.ImageField(upload_to=b'maps', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='phone_number',
            field=models.CharField(max_length=13, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='telephone',
            field=models.CharField(max_length=13, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='category',
            field=models.ForeignKey(to='main.Category', null=True),
        ),
    ]
