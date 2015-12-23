from django.db import models
from datetime import timedelta


class Routine(models.Model):

    name = models.CharField(max_length=255)
    total_time = models.DurationField(default=timedelta(), blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):

    name = models.CharField(max_length=255)
    completion_time = models.DurationField(default=timedelta())
    position = models.IntegerField()

    routine = models.ForeignKey(Routine)

    def __str__(self):
        return self.name