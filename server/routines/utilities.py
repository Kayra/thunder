from datetime import timedelta
from .models import Routine


def updateTotalTime(exercises):

    totalTime = timedelta(0)

    for exercise in exercises:
        totalTime += exercise.completion_time

    return totalTime
