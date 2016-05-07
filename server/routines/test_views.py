import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Routine, Exercise


def createExerciseForAPI(number=1):

    """
        Convinience function to create a test exercise
    """
    routine = Routine.objects.get(name='test2')

    exerciseToCreate = {}
    exerciseToCreate['name'] = 'textExercise' + str(number)
    exerciseToCreate['completion_time'] = '00:01:00'
    exerciseToCreate['position'] = str(number)
    exerciseToCreate['routine'] = routine.id

    return exerciseToCreate


class RoutineAPITests(TestCase):

    def setUp(self):

        exerciseNames = ['warm up', 'jog', 'run', 'jog', 'run']

        testRoutine1 = Routine.objects.create(name='test1', total_time='00:05:00')
        for index, exerciseName in enumerate(exerciseNames, start=1):
            Exercise.objects.create(name=exerciseName, completion_time='00:01:00', position=index, routine=testRoutine1)

        testRoutine2 = Routine.objects.create(name='test2', total_time='00:05:00')
        for index, exerciseName in enumerate(exerciseNames, start=1):
            Exercise.objects.create(name=exerciseName, completion_time='00:01:00', position=index, routine=testRoutine2)

    def test_get_routine_list(self):
        pass

    def test_get_routine(self):
        pass

    def test_create_routine(self):
        pass

    def test_edit_routine(self):
        pass

    def test_delete_routine(self):
        pass

    def test_get_exercise_list(self):
        pass

    def test_get_exercise(self):
        pass

    def test_create_exercise(self):
        pass

    def test_edit_exercise(self):
        pass

    def test_delete_exercise(self):
        pass

