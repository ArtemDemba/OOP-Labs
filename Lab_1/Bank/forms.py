from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'passport_number']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BankAccountForm(forms.ModelForm):

    class Meta:
        model = BankAccount
        fields = ('sum', 'bank')


class LoginFormBankSpec(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterBankSpec(UserCreationForm):

    class Meta:
        model = Applications
        fields = ('username', 'email', 'phone')
