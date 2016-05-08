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
        self.assertEquals(response.data['name'], routine_to_create['name'])

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
        pass

    def test_get_exercise(self):
        pass

    def test_create_exercise(self):
        pass

    def test_edit_exercise(self):
        pass

    def test_delete_exercise(self):
        pass
