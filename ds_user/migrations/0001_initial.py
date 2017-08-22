# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=None, max_length=50)),
                ('password', models.CharField(default=None, max_length=200)),
                ('state', models.IntegerField(default=0)),
                ('usertype', models.IntegerField(default=1)),
            ],
        ),
    ]
