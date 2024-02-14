from django.urls import path

from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms.views import CourseViewSet, index, LessonCreateAPIView, LessonListAPIView, LessonUpdateAPIView, \
    LessonRetrieveAPIView, LessonDestroyAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [path('', index, name='index'),
               path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
               path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
               path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
               path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='ls'),
               path('lesson/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_destroy'),

               ] + router.urls
