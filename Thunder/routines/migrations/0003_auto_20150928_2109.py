# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routines', '0002_auto_20150926_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='routine',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
