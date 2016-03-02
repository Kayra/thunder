# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('routines', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='routine',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='routine',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, related_name='routines'),
            preserve_default=False,
        ),
    ]
