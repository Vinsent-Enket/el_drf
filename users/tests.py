from django.test import TestCase
from django.urls import reverse


from lms.models import Lesson, Course
from users.models import User, Subscribe
from rest_framework.test import APITestCase

"""Для эндпоинтов работы с подпиской написаны тесты - этих тестов тоже не увидел"""


# Create your tests here.

class SubscribeTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test')
        # self.lesson = Lesson.objects.create(
        #     name='test',
        #     description='testtesttest',
        #     proprietor=self.user
        # )
        self.course = Course.objects.create(
            name='Test_course',
            description='Test_course_descr',
            proprietor=self.user
        )
        self.subscribe = Subscribe.objects.create(
            proprietor=self.user,
            courses=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_turn_subscribe(self):
        data = {
            'course_id': self.course.id
        }
        response = self.client.post(
            reverse('users:sub'),
            data=data
        )
        self.assertEqual(
            response.json(),
            {'message': f'Вы отписались от обновлений курса - {self.course.name}'}
        )
        response = self.client.post(
            reverse('users:sub'),
            data=data
        )
        self.assertEqual(
            response.json(),
            {'message': f'Вы подписались на курс - {self.course.name}'}
        )
        print(response.json())
