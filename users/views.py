from django_filters.rest_framework import filters, DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from config import settings
from config.permission import IsModerator
from lms.serializers import UserSerializer
from users.models import User, Transaction
from users.serializers import TransactionSerializer, MyTokenObtainPairSerializer
from rest_framework.filters import OrderingFilter


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsModerator]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsModerator]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsModerator]
    queryset = User.objects.all()


class TransactionListAPIView(ListAPIView):
    permission_classes = [IsModerator]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('purchased_course', 'purchased_lessons', 'payment_method',)
    ordering_fields = ('date',)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
