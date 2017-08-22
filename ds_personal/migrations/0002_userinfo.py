# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ds_personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField()),
                ('bitState', models.BigIntegerField()),
                ('realName', models.CharField(default=None, max_length=30)),
                ('idNumber', models.CharField(default=None, max_length=30)),
                ('phoneNumber', models.CharField(default=None, max_length=30)),
                ('authScore', models.IntegerField(default=None)),
                ('email', models.CharField(default=None, max_length=255)),
                ('educationBackground', models.ForeignKey(related_name='educationBackground_id', default=None, to='ds_personal.SystemDictionaryItem')),
                ('houseCondition', models.ForeignKey(related_name='houseCondition_id', default=None, to='ds_personal.SystemDictionaryItem')),
                ('incomeGrade', models.ForeignKey(related_name='incomeGrade_id', default=None, to='ds_personal.SystemDictionaryItem')),
                ('kidCount', models.ForeignKey(related_name='kidCount_id', default=None, to='ds_personal.SystemDictionaryItem')),
                ('marriage', models.ForeignKey(related_name='marriage_id', default=None, to='ds_personal.SystemDictionaryItem')),
                ('realAuth', models.ForeignKey(default=None, to='ds_personal.RealAuth')),
            ],
        ),
    ]
