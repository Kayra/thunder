from datetime import timedelta

from .models import Routine, Exercise


def calculateTotalTime(exercises):

    totalTime = timedelta(0)

    for exercise in exercises:
        totalTime += exercise.completion_time

    return totalTime


def updateTotalTime(routineId):

    routine = Routine.objects.get(id=routineId)
    exercises = Exercise.objects.filter(routine=routine)
    totalTime = calculateTotalTime(exercises)
    routine.total_time = totalTime
    routine.save()
