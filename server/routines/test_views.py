import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from .models import Routine, Exercise


def createExerciseForAPI(number=1):

    """
    Convenience function to create a test exercise object to be submitted to the API.
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

        self.testUser = User.objects.create(username='test', email='test@test.com', password='test123')

        exerciseNames = ['warm up', 'jog', 'run', 'jog', 'run']

        testRoutine1 = Routine.objects.create(name='test1', total_time='00:05:00', user=self.testUser)
        for index, exerciseName in enumerate(exerciseNames, start=1):
            Exercise.objects.create(name=exerciseName, completion_time='00:01:00', position=index, routine=testRoutine1)

        testRoutine2 = Routine.objects.create(name='test2', total_time='00:05:00', user=self.testUser)
        for index, exerciseName in enumerate(exerciseNames, start=1):
            Exercise.objects.create(name=exerciseName, completion_time='00:01:00', position=index, routine=testRoutine2)

        self.client.force_login(user=self.testUser)

    def test_get_routine_list(self):

        url = reverse('routines:routine_list_create')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

        database_routine_ids = [routine.id for routine in Routine.objects.all()]
        response_routine_ids = [routine['id'] for routine in response.data]
        self.assertCountEqual(database_routine_ids, response_routine_ids)

    def test_get_routine(self):
        routine = Routine.objects.order_by('id')[0]
        url = reverse('routines:routine_detail', kwargs={'pk': routine.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(routine.id, response.data['id'])

    def test_create_routine(self):

        routine_to_create = {
            'name': 'test3',
            'total_time': '00:15:00',
            'user': self.testUser.id
        }

        url = reverse('routines:routine_list_create')
        response = self.client.post(url, routine_to_create)
        self.assertEquals(response.status_code, 201)
        self.assertTrue(Routine.objects.get(name=routine_to_create['name']))

    def test_edit_routine(self):

        routine_to_edit = Routine.objects.order_by('id')[0]

        edited_routine = {
            'name': 'edited',
            'total_time': '0' + str(routine_to_edit.total_time),
            'user': routine_to_edit.user.id
        }

        url = reverse('routines:routine_detail', kwargs={'pk': routine_to_edit.id})
        response = self.client.put(url, json.dumps(edited_routine), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['name'], edited_routine['name'])

    def test_delete_routine(self):

        routine_to_delete = Routine.objects.order_by('id')[0]

        url = reverse('routines:routine_detail', kwargs={'pk': routine_to_delete.id})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        with self.assertRaises(Routine.DoesNotExist):
            Routine.objects.get(pk=routine_to_delete.id)

    def test_get_exercise_list(self):
        routine = Routine.objects.order_by('id')[0]
        url = reverse('routines:exercise_list_create')
        response = self.client.get(url, {'routineId': routine.id})
        self.assertEquals(response.status_code, 200)
        database_exercise_ids = [exercise.id for exercise in Exercise.objects.filter(routine=routine)]
        response_exercise_ids = [exercise['id'] for exercise in response.data]
        self.assertCountEqual(database_exercise_ids, response_exercise_ids)

    def test_get_exercise(self):
        exercise = Exercise.objects.order_by('id')[0]
        url = reverse('routines:exercise_detail', kwargs={'pk': exercise.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(exercise.id, response.data['id'])

    def test_create_exercise(self):

        routine = Routine.objects.order_by('id')[0]
        exercise_to_create = {
            'name': 'test',
            'completion_time': '00:01:30',
            'position': '6',
            'routine': routine.id
        }

        url = reverse('routines:exercise_list_create')
        response = self.client.post(url, exercise_to_create)
        self.assertEquals(response.status_code, 201)
        self.assertTrue(Exercise.objects.get(name=exercise_to_create['name']))

    def test_create_exercise_many(self):

        routine = Routine.objects.order_by('id')[0]

        exercises_to_create = [
            {
                'name': 'test1',
                'completion_time': '00:01:45',
                'position': '6',
                'routine': str(routine.id),
            },
            {
                'name': 'test2',
                'completion_time': '00:02:15',
                'position': '7',
                'routine': str(routine.id),
            },
        ]

        url = reverse('routines:exercise_create_many')
        response = self.client.post(url, json.dumps(exercises_to_create), content_type='application/json')
        self.assertEquals(response.status_code, 201)
        database_exercise_ids = [exercise.id for exercise in Exercise.objects.filter(routine=routine)]
        response_exercise_ids = [exercise['id'] for exercise in response.data]
        self.assertEquals(len(set(response_exercise_ids) - set(database_exercise_ids)), 0)

    def test_edit_exercise(self):

        exercise = Exercise.objects.order_by('id')[0]

        exercise_to_edit = {
            'name': 'edited',
            'completion_time': '0' + str(exercise.completion_time),
            'position': exercise.position,
            'routine': str(exercise.routine.id),
        }

        url = reverse('routines:exercise_detail', kwargs={'pk': exercise.id})
        response = self.client.put(url, json.dumps(exercise_to_edit), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(Exercise.objects.get(name='edited'))

    def test_delete_exercise(self):
        exercise = Exercise.objects.order_by('id')[0]
        url = reverse('routines:exercise_detail', kwargs={'pk': exercise.id})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        with self.assertRaises(Exercise.DoesNotExist):
            Exercise.objects.get(pk=exercise.id)
