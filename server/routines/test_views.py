import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Routine, Exercise


def createExerciseForAPI(number=1):

    """
        Convinience function to create a test exercise
    """

    exerciseToCreate = {}
    exerciseToCreate['name'] = 'textExercise' + str(number)
    exerciseToCreate['completion_time'] = '00:01:00'
    exerciseToCreate['position'] = str(number)
    exerciseToCreate['routine'] = 'test2'

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

    def test_getRoutines(self):

        """
            All routines should be returned
        """

        url = reverse('routines:get_routines')

        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)  # Make sure valid request returns success response

        routinesFromDB = Routine.objects.all()
        self.assertEquals(routinesFromDB, response.data)  # Make sure routines from API match routines in routinesFromDbS

    def test_getRoutine(self):

        """
            A routine and associated exercises should be returned when a correct id is passed as a parameter
        """

        url = reverse('routines:get_routine')

        response = self.client.post(url, {'wrong': 'wrong'})
        self.assertEquals(response.status_code, 400)  # Make sure bad params return error response

        routineFromDB = Routine.objects.all()[:1].get()
        response = self.client.get(url, {'id': routineFromDB.id})
        self.assertEquals(response.status_code, 200)  # Make sure valid request returns success response

        data = json.loads(response.content.decode())
        self.assertEquals(routineFromDB, data)  # Make sure the correct routine was returned

    def test_createRoutine(self):

        """
            A routine created with the API should be in the database
        """

        url = reverse('routines:create_routine')

        response = self.client.post(url)
        self.assertEquals(response.status_code, 400)  # Make sure no params return error response

        response = self.client.post(url, {'wrong': 'wrong'})
        self.assertEquals(response.status_code, 400)  # Make sure bad params return error response

        routineToCreate = {}
        routineToCreate['name'] = 'test3'
        response = self.client.post(url, routineToCreate)
        self.assertEquals(response.status_code, 200)  # Make sure valid request returns success response

        routineFromDB = Routine.objects.get(pk=response.data['id'])
        self.assertEquals(routineFromDB.name, response.data['name'])  # Make sure the routine created via the API is in the DB

    def test_deleteRoutine(self):

        """
            A routine deleted with the API should not be in the database
        """

        url = reverse('routines:delete_routine')

        response = self.client.delete(url, {'wrong': 'wrong'})
        self.assertEquals(response.status_code, 400)  # Make sure bad parameters return error response

        routineToDelete = Routine.objects.all()[:1].get()
        routineToDeleteJson = json.dumps({'id': routineToDelete.id})
        response = self.client.delete(url, routineToDeleteJson)
        self.assertEquals(response.status_code, 204)  # Make sure valid request returns success response

        with self.assertRaises(Routine.DoesNotExist):
            Routine.objects.get(pk=routineToDelete.id)  # Make sure the routine no longer exists in the DB

    def test_createExercises(self):

        """
            All exercises created with the API should be in the database
        """

        url = reverse('routines:create_exercises')

        response = self.client.post(url)
        self.assertEquals(response.status_code, 400)  # Make sure no params return error response

        response = self.client.post(url, {'wrong': 'wrong'})
        self.assertEquals(response.status_code, 400)  # Make sure bad params return error response

        exercisesToCreate = []
        for index in range(0, 3):
            exercisesToCreate.append(createExerciseForAPI(index))
        response = self.client.post(url, exercisesToCreate)
        self.assertEquals(response.status_code, 200)  # Make sure valid request returns success response

        exercisesFromDB = Exercise.objects.get(routine=response.data[0]['routine'])
        self.assertEquals(exercisesFromDB, response.data)  # Make sure the exercises created via the API are in the DB

    def test_createExercise(self):

        """
            An exercise created with the API should be in the database
        """

        url = reverse('routines:create_exercise')

        response = self.client.post(url)
        self.assertEquals(response.status_code, 400)  # Make sure no params return error response

        response = self.client.post(url, {'wrong': 'wrong'})
        self.assertEquals(response.status_code, 400)  # Make sure bad params return error response

        exerciseToCreate = createExerciseForAPI()
        response = self.client.post(url, exerciseToCreate)
        self.assertEquals(response.status_code, 200)  # Make sure valid request returns success response

        exerciseFromDB = Exercise.objects.get(routine=response.data['routine'])
        self.assertEquals(exerciseFromDB, response.data)  # Make sure the exercise created via the API is in the DB

    def test_deleteExercise(self):

        """
            An exercise deleted with the API should not be in the database
        """

        url = reverse('routines:delete_exercise')

        response = self.client.post(url)
        self.assertEquals(response.status_code, 400)  # Make sure no params return error response

        response = self.client.delete(url, {'wrong': 'wrong'})
        self.assertEquals(response.status_code, 400)  # Make sure bad parameters return error response

        exerciseToDelete = Exercise.objects.all()[:1].get()
        exerciseToDeleteJson = json.dumps({'id': exerciseToDelete.id})
        response = self.client.delete(url, exerciseToDeleteJson)
        self.assertEquals(response.status_code, 204)  # Make sure valid request returns success response

        with self.assertRaises(Exercise.DoesNotExist):
            Exercise.objects.get(pk=exerciseToDelete.id)  # Make sure the exercise no longer exists in the DB
