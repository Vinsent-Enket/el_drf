from django.http import request
from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config import settings
from lms.models import Lesson, Course
from lms.paginators import LMSPagination
from lms.serializers import LessonSerializer, CourseSerializer
from users import servises
from users.permission import IsModerator, IsProprietor


# Create your views here.

def index(request):
    return render(request, 'lms/index.html')


class CourseViewSet(viewsets.ModelViewSet):
    pagination_class = LMSPagination
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseSerializer(paginated_queryset, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)

    def perform_create(self, serializer):
        stripe_product_id = servises.create_stripe_product(self.request.data['name'])
        stripe_price_id = servises.create_stripe_price(stripe_product_id, self.request.data['price'])
        serializer.save(stripe_product_id=stripe_product_id, stripe_price_id=stripe_price_id)

    def get_permissions(self):
        if self.action == 'create':
            #self.permission_classes = [IsAuthenticated, ~IsModerator]
            self.permission_classes = [IsAuthenticated]

        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsProprietor | IsModerator]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsProprietor | IsModerator]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsProprietor | IsModerator]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated, IsProprietor | IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsProprietor]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ~IsModerator]
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    pagination_class = LMSPagination
    permission_classes = [IsAuthenticated, IsProprietor | IsModerator]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get(self, request, **kwargs):
        queryset = Lesson.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LessonSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsProprietor | IsModerator]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsProprietor | IsModerator]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsProprietor]
    queryset = Lesson.objects.all()
