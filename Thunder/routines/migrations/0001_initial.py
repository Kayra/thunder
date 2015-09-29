# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Skill name', max_length=255)),
                ('completion_time', models.DurationField(default=datetime.timedelta(0))),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Skill name', max_length=255)),
                ('total_time', models.DurationField(blank=True, default=datetime.timedelta(0))),
            ],
        ),
    ]
