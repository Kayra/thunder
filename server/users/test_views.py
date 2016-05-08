import json

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class RoutineAPITests(TestCase):

    def setUp(self):
        testUser = User.objects.create(username='test', email='test@test.com', password='test123')

    def test_get_user(self):
        pass

    def test_create_user(self):
        pass

    def test_edit_user(self):
        pass

    def test_delete_user(self):
        pass

    def test_auth_user(self):
        pass
