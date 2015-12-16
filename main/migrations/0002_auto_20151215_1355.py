# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='url',
            field=models.CharField(default=1, max_length=100, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brands',
            name='url',
            field=models.CharField(default=1, max_length=100, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='production',
            name='url',
            field=models.CharField(default=1, max_length=100, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productionelecticsimple',
            name='url',
            field=models.CharField(default=1, max_length=100, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='url',
            field=models.CharField(default=1, max_length=100, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=False,
        ),
    ]
