from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput

from .models import Customer

class CustomerCreation(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'adress', 'phone_number']





class CustomerChange(UserChangeForm):
    class Meta(UserChangeForm):
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email', 'adress', 'phone_number')
