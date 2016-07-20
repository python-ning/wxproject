# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wx_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=30, verbose_name=b'openid')),
                ('nickname', models.CharField(max_length=30, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1\xe5\x90\x8d')),
                ('sex', models.CharField(max_length=30, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('language', models.CharField(max_length=30, verbose_name=b'\xe8\xaf\xad\xe8\xa8\x80')),
                ('city', models.CharField(max_length=30, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82')),
                ('province', models.CharField(max_length=30, verbose_name=b'\xe7\x9c\x81\xe4\xbb\xbd')),
                ('country', models.CharField(max_length=30, verbose_name=b'\xe5\x9b\xbd\xe5\xae\xb6')),
                ('headimgurl', models.CharField(max_length=30, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
                ('privilege', models.CharField(max_length=30, verbose_name=b'\xe7\x89\xb9\xe6\x9d\x83')),
            ],
        ),
    ]
