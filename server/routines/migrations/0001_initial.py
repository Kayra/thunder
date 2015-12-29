# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('completion_time', models.DurationField(default=datetime.timedelta(0))),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_time', models.DurationField(default=datetime.timedelta(0), blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='routine',
            field=models.ForeignKey(to='routines.Routine'),
        ),
    ]
