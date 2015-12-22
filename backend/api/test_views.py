import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Routine, Exercise


class RoutineAPITests(TestCase):

    def setUp(self):
        Routine.objects.create(name='test1', total_time='0:05:00')
        Exercise.objects.create(name='warm up', completion_time='0:01:00', position=1, routine__name='test1')
        Exercise.objects.create(name='jog', completion_time='0:01:00', position=2, routine__name='test1')
        Exercise.objects.create(name='run', completion_time='0:01:00', position=3, routine__name='test1')
        Exercise.objects.create(name='jog', completion_time='0:01:00', position=4, routine__name='test1')
        Exercise.objects.create(name='run', completion_time='0:01:00', position=5, routine__name='test1')

        Routine.objects.create(name='test2', total_time='0:05:00')
        Exercise.objects.create(name='warm up', completion_time='0:01:00', position=1, routine__name='test2')
        Exercise.objects.create(name='jog', completion_time='0:01:00', position=2, routine__name='test2')
        Exercise.objects.create(name='run', completion_time='0:01:00', position=3, routine__name='test2')
        Exercise.objects.create(name='jog', completion_time='0:01:00', position=4, routine__name='test2')
        Exercise.objects.create(name='run', completion_time='0:01:00', position=5, routine__name='test2')

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

        routineToCreate = {}
        routineToCreate['name'] = 'test3'

        url = reverse('females:create_routine')

        response = self.client.post(url)
        self.assertEquals(response.status_code, 400)  # Make sure no params return error response

        response = self.client.post(url, {'wrong': 'wrong'})
        self.assertEquals(response.status_code, 400)  # Make sure bad params return error response

        response = self.client.post(url, routineToCreate)
        self.assertEquals(response.status_code, 200)  # Make sure valid request returns success response

        routineFromDB = Routine.objects.get(pk=response.data['id'])
        self.assertEquals(routineFromDB.name, response.data['name'])  # Make sure the routine created via the API is in the DB

    def test_deleteRoutine(self):
        pass

    def test_createExercises(self):
        pass

    def test_createExercise(self):
        pass

    def test_deleteExercise(self):
        pass


 # def test_getFemale(self):

 #        """
 #            A female should be returned when a correct id is passed as a parameter
 #        """

 #        testFemale = Female.objects.all()[:1].get()
 #        testIdentifier = testFemale.id

 #        url = reverse('females:get_female')

 #        response = self.client.get(url)
 #        self.assertEquals(response.status_code, 400)  # Make sure no params return error response

 #        response = self.client.get(url, {'wrong': 'wrong'}, content_type='application/json')
 #        self.assertEquals(response.status_code, 400)  # Make sure bad params return error response

 #        response = self.client.get(url, {'identifier': testIdentifier})
 #        self.assertEquals(response.status_code, 200)  # Make sure valid request returns success response

 #        data = json.loads(response.content.decode())
 #        self.assertEquals(len(data), 6)  # Make sure all fields are present

 #        self.assertEquals(testIdentifier, data['id'])  # Make sure the correct female was returned
