import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from lms.models import Lesson, Course
from users.models import User, Subscribe


class LessonTestCase(APITestCase):
    """Почему то создается слишком много урокаов, как будто после каждого теста"""

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test')
        self.lesson = Lesson.objects.create(
            name='test',
            description='testtesttest',
            proprietor=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_create_create(self):
        data = {"name": "test_name",
                "description": "test_descr"}

        response = self.client.post(
            reverse("lms:lesson_create"),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2, 'name': 'test_name', 'description': 'test_descr', 'preview': None, 'video_url': None,
             'created_at': '2024-03-06', 'proprietor': None}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
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
        self.assertEqual(
            response.json(),

            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lesson.id,
                 'name': self.lesson.name,
                 'description': self.lesson.description,
                 'preview': None,
                 'video_url': None,
                 'created_at': '2024-03-06',
                 'proprietor': self.user.id}]}
        )

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('lms:lessons_list')
        )
        response = self.client.patch(
            reverse('lms:ls', args=[self.lesson.id]),
            data={'name': 'test_name', 'description': 'test_descr', }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 5, 'name': 'test_name', 'description': 'test_descr', 'preview': None, 'video_url': None,
             'created_at': '2024-03-06', 'proprietor': 4}
        )

    def test_delete_lesson(self):
        response = self.client.delete(
            reverse('lms:lesson_destroy', args=[self.lesson.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
