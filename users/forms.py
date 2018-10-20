from django import forms
from django.contrib.auth.models import User
from .models import *


# CONSTANT
# PARAMETERS
ERROR_MESSAGE_USER = {
    'required': 'Username is required',
    'unique': 'That Username is not available, try another one',
    'invalid': 'The Username format is incorrect, try another one'
}

ERROR_MESSAGE_PASSWORD = {
    'required': 'Password is required',
    'invalid': 'The Password format is incorrect, password must be at leat 8 characters long and contain a number or a symbol'
}

ERROR_MESSAGE_EMAIL = {
    'required': 'Email is required',
    'unique': 'That Email adress is already registered, try another one',
    'invalid': 'The Email format incorrect, try a valid email adress'
}


# FORMS
# LOGIN
class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


# CREATE USER
class CreateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, error_messages=ERROR_MESSAGE_USER)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(), error_messages=ERROR_MESSAGE_PASSWORD)
    email = forms.CharField(error_messages=ERROR_MESSAGE_EMAIL)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'user_type')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count():
            raise forms.ValidationError('That email is already registered in other account')
        return email
