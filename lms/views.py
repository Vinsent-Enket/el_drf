from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from config.permission import IsProprietor
from lms.models import Lesson, Course
from lms.serializers import LessonSerializer, CourseSerializer
from users.permission import IsModerator


# Create your views here.

def index(request):
    return render(request, 'lms/index.html')


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsProprietor, IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsProprietor]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsProprietor]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsProprietor]
    queryset = Lesson.objects.all()
