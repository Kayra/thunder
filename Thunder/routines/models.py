from __future__ import absolute_import
from datetime import timedelta

from django.db import models
from Thunder.users.models import User


class Routine(models.Model):

    name                = models.CharField("Skill name", max_length=255)
    total_time          = models.DurationField(default=timedelta(), blank=True)

    user                = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Exercise(models.Model):

    name                = models.CharField("Skill name", max_length=255)
    completion_time     = models.DurationField(default=timedelta())
    position            = models.IntegerField()

    routine             = models.ForeignKey(Routine)

    def __unicode__(self):
        return self.name
