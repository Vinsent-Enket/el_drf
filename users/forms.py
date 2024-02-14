from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('self_email', 'work_email', 'first_name', 'last_name',  'password1', 'password2', )


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('self_email', 'work_email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
