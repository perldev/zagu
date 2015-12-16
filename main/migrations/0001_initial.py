# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('introtext', models.TextField()),
                ('meta_keyword', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.CharField(max_length=255, blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0410\u0443\u0434\u0438\u043e')),
                ('audio', models.FileField(upload_to=b'audio')),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audio',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Alt \u0437\u0430\u0433\u0430\u043b\u043e\u0432\u043e\u043a')),
                ('img', models.ImageField(upload_to=b'banners_sq', verbose_name='\u0411\u0430\u043d\u043d\u0435\u0440')),
                ('url', models.CharField(default=b'#', max_length=255, null=True, blank=True)),
                ('is_pub', models.CharField(default=b'no', max_length=5, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d', choices=[(b'yes', '\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d'), (b'no', '\u041d\u0435 \u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d')])),
            ],
            options={
                'verbose_name': '\u0411\u0430\u043d\u043d\u0435\u0440',
                'verbose_name_plural': '\u0411\u0430\u043d\u043d\u0435\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('path', models.ImageField(upload_to=b'banners', verbose_name='\u0411\u0430\u043d\u043d\u0435\u0440')),
                ('ordering', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434 - \u043c\u0435\u043d\u044e',
            },
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0411\u0440\u0435\u043d\u0434',
                'verbose_name_plural': '\u0411\u0440\u0435\u043d\u0434',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='CustomMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255, verbose_name='\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 url')),
                ('meta_keyword', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.CharField(max_length=255, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u0430\u043b\u043e\u0432\u043e\u043a')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0442\u043e\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u041c\u0435\u0442\u0430 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0434\u043b\u044f Url',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.ImageField(upload_to=b'files', verbose_name='Photo')),
                ('path_thumb', models.ImageField(upload_to=b'files/thumb', verbose_name='Small Photo', blank=True)),
                ('order', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430', blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImagesSimple',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.ImageField(upload_to=b'simple_catalog', verbose_name='Photo')),
                ('order', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430', blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Alt \u0437\u0430\u0433\u0430\u043b\u043e\u0432\u043e\u043a')),
                ('img', models.ImageField(upload_to=b'art_images', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0443',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='PresentetionImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.ImageField(upload_to=b'present_files', verbose_name='Photo')),
                ('order', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PresentPartn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('meta_keyword', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.CharField(max_length=255, blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u041f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('meta_keyword', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.CharField(max_length=255, blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
                ('ordering', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('introtext', models.TextField()),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f',
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='ProductionElecticSimple',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0437\u0438\u0446\u0438\u0438')),
                ('text', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('power', models.CharField(max_length=40, verbose_name='\u043f\u043e\u0442\u0440\u0435\u0431\u043b\u044f\u0435\u043c\u0430\u044f \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u044c', blank=True)),
                ('price', models.DecimalField(default=0, verbose_name='\u0426\u0435\u043d\u0430', max_digits=18, decimal_places=2)),
                ('currency', models.CharField(default=b'USD', max_length=24, verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430', choices=[(b'UAH', '\u0413\u0420\u041d'), (b'USD', 'USD'), (b'EUR', 'EUR')])),
                ('meta_keyword', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.CharField(max_length=255, blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
                ('ordering', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('brand', models.ForeignKey(verbose_name='\u0411\u0440\u0435\u043d\u0434', to='main.Brands')),
                ('thumb', models.ForeignKey(verbose_name='Photo', blank=True, to='main.ImagesSimple', null=True)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f \u0432\u0441\u043f\u043e\u043c\u043e\u0433\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f',
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f \u0432\u0441\u043f\u043e\u043c\u043e\u0433\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f',
            },
        ),
        migrations.CreateModel(
            name='ProductionMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('url_item', models.CharField(max_length=255, null=True, verbose_name='Url \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True)),
                ('item', models.ForeignKey(blank=True, to='main.Production', null=True)),
            ],
            options={
                'verbose_name': '\u042d\u043b\u0435\u043c\u0435\u043d\u0442 \u043c\u0435\u043d\u044e \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='ProductionMenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('url_item', models.CharField(max_length=255, null=True, verbose_name='Url \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True)),
                ('ordering', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('item', models.ForeignKey(blank=True, to='main.Production', null=True)),
                ('root', models.ForeignKey(to='main.ProductionMenu')),
            ],
            options={
                'verbose_name': '\u042d\u043b\u0435\u043c\u0435\u043d\u0442 \u043c\u0435\u043d\u044e \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='ProductionSimpleCatalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archive', models.FileField(upload_to=b'catalogs', verbose_name='Rar  \u0430\u0440\u0445\u0438\u0432 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
                ('status', models.CharField(default=b'no', max_length=5, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d', choices=[(b'yes', '\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d'), (b'no', '\u041d\u0435 \u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d')])),
                ('brand', models.ForeignKey(verbose_name='\u0411\u0440\u0435\u043d\u0434', to='main.Brands')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0430\u043b\u043e\u0433',
                'verbose_name_plural': '\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('meta_keyword', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.CharField(max_length=255, blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0435\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ProjectsImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.ImageField(upload_to=b'projects_files', verbose_name='Photo')),
                ('order', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430', blank=True)),
                ('article', models.ForeignKey(to='main.Projects')),
            ],
        ),
        migrations.AddField(
            model_name='presentetionimages',
            name='article',
            field=models.ForeignKey(to='main.PresentPartn'),
        ),
        migrations.AddField(
            model_name='imagessimple',
            name='article',
            field=models.ForeignKey(to='main.ProductionElecticSimple', null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='article',
            field=models.ForeignKey(to='main.Production'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(to='main.Category'),
        ),
    ]
