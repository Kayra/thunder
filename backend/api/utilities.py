from datetime import timedelta


def updateTotalTime(exercises):

    totalTime = timedelta(0)

    for exercise in exercises:
        totalTime += exercise.completion_time

    return totalTime
