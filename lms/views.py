from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from config.permission import IsModerator, IsProprietor
from lms.models import Lesson, Course
from lms.serializers import LessonSerializer, CourseSerializer


# Create your views here.

def index(request):
    return render(request, 'lms/index.html')


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'list':
            self.permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            self.permission_classes = [AllowAny]
        elif self.action == 'update':
            self.permission_classes = [IsModerator, IsProprietor]
        elif self.action == 'destroy':
            self.permission_classes = [IsModerator, IsProprietor]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsModerator]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsModerator, IsProprietor]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser, IsProprietor]
    queryset = Lesson.objects.all()
