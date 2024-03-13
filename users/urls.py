from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    TransactionListAPIView, \
    MyTokenObtainPairView, SubscribeAPIView, TransactionAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', UserCreateAPIView.as_view(), name='user_create'),
    path('profile/<int:pk>/', UserRetrieveAPIView.as_view(), name='profile'),
    path('profile_update/<int:pk>/', UserUpdateAPIView.as_view(), name='profile_update'),
    path('profile_list/', UserListAPIView.as_view(), name='profile_list'),
    path('subscribe/', SubscribeAPIView.as_view(), name='sub'),

    # урлы для транзакций
    path('transaction_list/', TransactionListAPIView.as_view(), name='transaction_list'),
    # новые урлы для пользователя
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('pay/', TransactionAPIView.as_view(), name='pay')

]
