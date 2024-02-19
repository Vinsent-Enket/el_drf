from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.views import RegistrationView, ProfileView, VerifyEmailView, generate_new_password, \
    UserForgotPasswordView, UserPasswordResetConfirmView, registration_info, TransactionListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('registration_info/', registration_info, name='registration_info'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify_email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # урлы для транзакций
    path('transaction/', TransactionListAPIView.as_view(), name='transaction_list'),

]
