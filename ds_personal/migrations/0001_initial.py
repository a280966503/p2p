# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ds_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realname', models.CharField(max_length=50)),
                ('sex', models.IntegerField()),
                ('birthDate', models.CharField(max_length=50)),
                ('idNumber', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('state', models.IntegerField()),
                ('image1', models.CharField(max_length=255)),
                ('image2', models.CharField(max_length=255)),
                ('remark', models.CharField(default=None, max_length=255)),
                ('auditTime', models.DateTimeField(default=None)),
                ('applyTime', models.DateTimeField()),
                ('applier', models.ForeignKey(related_name='applier_id', to='ds_user.LoginInfo')),
                ('auditor', models.ForeignKey(related_name='auditor_id', default=None, to='ds_user.LoginInfo')),
            ],
        ),
        migrations.CreateModel(
            name='SystemDictionary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SystemDictionaryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('sequence', models.IntegerField()),
                ('parent', models.ForeignKey(to='ds_personal.SystemDictionary')),
            ],
        ),
    ]
