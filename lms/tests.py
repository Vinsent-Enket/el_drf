from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from lms.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_superuser=True)

        self.lesson = Lesson.objects.create(
            name='test',
            description='testtesttest'
        )

    def test_get_list(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('lms:lessons_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
