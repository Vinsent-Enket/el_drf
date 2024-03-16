from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import ListAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from lms.models import Course
from users import servises
from users.permission import IsTrueUser, IsModerator, IsProprietor
from users.models import User, Transaction, Subscribe
from users.serializers import TransactionSerializer, MyTokenObtainPairSerializer, UserSerializer, SubscribeSerializer
from rest_framework.filters import OrderingFilter


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsTrueUser, IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsTrueUser, IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsTrueUser, IsAuthenticated]
    queryset = User.objects.all()


class TransactionListAPIView(ListAPIView):
    permission_classes = [IsModerator, IsAuthenticated]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('purchased_course', 'purchased_lessons', 'payment_method',)
    ordering_fields = ('date',)


class SubscribeCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsProprietor, ~IsModerator]
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()


class SubscribeRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsProprietor]
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()


class SubscribeUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsProprietor]
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()


class SubscribeAPIView(APIView):
    permission_classes = [IsAuthenticated, ~IsModerator]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        try:
            subscribe = Subscribe.objects.get(proprietor=user, courses=course)
        except Subscribe.DoesNotExist:

            subscribe = Subscribe(
                proprietor=user,
                courses=course
            )
            subscribe.save()
            message = f'Вы подписались на курс - {course.name}'
        else:
            subscribe.delete()
            message = f'Вы отписались от обновлений курса - {course.name}'

        return Response({'message': message})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class TransactionCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.request.data['course_id'])
        stripe_price_id = course.stripe_price_id
        # получаем из запроса на оплату id курса и получаем ссылку на прайс
        stripe_session = servises.get_payment_link(stripe_price_id)
        url_to_pay = stripe_session['url']
        serializer.save(strip_session_id=stripe_session['id'], user=self.request.user, url_to_pay=url_to_pay)


class TransactionPayAPIView(APIView):
    def post(self, *args, **kwargs):
        transaction_id = self.request.data.get('transaction_id')
        user = self.request.user
        try:
            transaction = Transaction.objects.get(user=user, id=transaction_id)
            amount = transaction.payment_amount
        except Transaction.DoesNotExist:
            message = f'Неверный ID покупки - {transaction_id}'
        else:
            # courses_names = [lesson.name for lesson in transaction.purchased_course.objects.all()]
            # lessons_names = [lesson.name for lesson in transaction.purchased_lessons.objects.all()] #как мне вытащить названия?
            # names = ', '.join(courses_names+lessons_names)
            names = 'Курсы и уроки заявленные к покупке'

        return Response({'message': message})
