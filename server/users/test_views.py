import json

from django.core.urlresolvers import reverse, NoReverseMatch
from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework_jwt.settings import api_settings


class UserAPITests(TestCase):

    def setUp(self):
        user = User(username="initial_tester", email="initial_tester@test.com")
        user.set_password("initial_tester123")
        user.save()

        self.edited_user = {
            'id': user.id,
            'username': 'edited',
            'email': user.email
        }

        self.client.force_login(user=user)

    def test_get_user_no_parameters(self):
        with self.assertRaises(NoReverseMatch):
            reverse('users:user_detail')

    def test_get_user_invalid_parameters(self):
        with self.assertRaises(NoReverseMatch):
            reverse('users:user_detail', kwargs={'invalid': 'invalid'})

    def test_get_user_doesnt_exist(self):
        url = reverse('users:user_detail', kwargs={'pk': '959'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_get_user_does_exist(self):

        user = User.objects.get(username='initial_tester')

        url = reverse('users:user_detail', kwargs={'pk': user.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_create_user_invalid_parameters(self):
        url = reverse('users:user_create')
        response = self.client.post(url, {'invalid': 'invalid'})
        self.assertEquals(response.status_code, 400)

    def test_create_user_valid_parameters(self):

        test_user = {
            'username': 'tester',
            'email': 'tester@test.com',
            'password': 'tester123'
        }

        url = reverse('users:user_create')
        response = self.client.post(url, test_user)
        self.assertEquals(response.status_code, 201)
        self.assertTrue(User.objects.get(username=test_user['username']))

    def test_update_user_no_parameters(self):
        with self.assertRaises(NoReverseMatch):
            reverse('users:user_detail')

    def test_update_user_invalid_parameters(self):
        with self.assertRaises(NoReverseMatch):
            reverse('users:user_detail', kwargs={'invalid': 'invalid'})

    def test_update_user_nonexistant_pk(self):
        url = reverse('users:user_detail', kwargs={'pk': '959'})
        response = self.client.patch(url, self.edited_user)
        self.assertEquals(response.status_code, 404)
        response = self.client.put(url, self.edited_user)
        self.assertEquals(response.status_code, 404)

    def test_update_user_valid_parameters_patch(self):
        url = reverse('users:user_detail', kwargs={'pk': self.edited_user['id']})
        response = self.client.patch(url, json.dumps(self.edited_user), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], User.objects.get(username=self.edited_user['username']).id)

    def test_update_user_valid_parameters_put(self):

        edited_user_put = self.edited_user
        edited_user_put['password'] = User.objects.get(id=edited_user_put['id']).password

        url = reverse('users:user_detail', kwargs={'pk': edited_user_put['id']})
        response = self.client.put(url, json.dumps(edited_user_put), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], User.objects.get(username=edited_user_put['username']).id)

    def test_delete_user_no_parameters(self):
        with self.assertRaises(NoReverseMatch):
            reverse('users:user_detail')

    def test_delete_user_invalid_parameters(self):
        with self.assertRaises(NoReverseMatch):
            reverse('users:user_detail', kwargs={'invalid': 'invalid'})

    def test_delete_user_valid_parameters(self):

        test_user = User.objects.get(username='initial_tester')

        url = reverse('users:user_detail', kwargs={'pk': test_user.pk})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='initial_tester')

    def test_user_auth_no_params(self):
        url = reverse('users:user_auth')
        response = self.client.post(url)
        self.assertEquals(response.status_code, 400)

    def test_user_auth_invalid_params(self):
        url = reverse('users:user_auth')
        response = self.client.post(url, {'invalid': 'invalid'})
        self.assertEquals(response.status_code, 400)

    def test_user_auth_invalid_login(self):
        url = reverse('users:user_auth')
        response = self.client.post(url, {'username': 'invalid'})
        self.assertEquals(response.status_code, 400)

    def test_user_auth_valid_login(self):
        url = reverse('users:user_auth')
        response = self.client.post(url, {'username': 'initial_tester', 'password': 'initial_tester123'})
        self.assertEquals(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_user_auth_token(self):
        user = User.objects.get(username='initial_tester')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)

        url = reverse('users:user_auth')
        response = self.client.post(url, {'username': 'initial_tester', 'password': 'initial_tester123'})
        self.assertEquals(jwt_encode_handler(payload), response.data['token'])
