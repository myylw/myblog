from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import get_user_model
from django.forms import TextInput, PasswordInput, EmailInput
from django import forms


class UserCreateForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'nick_name', 'email']


class UserUpdateForm(UserChangeForm):
    pass

class UserLoginForm(AuthenticationForm):
    pass

