from django.forms import ModelForm, Select, TextInput
from .models import Shipping_Adress

class Shipping_AdressForm(ModelForm):
    class Meta:
        model = Shipping_Adress
        fields = ('adress', 'city', 'state', 'zip_code', 'phone_number')

        widgets = {
            'adress': TextInput(
                attrs={
                    'name': 'adress',
                    'placeholder': "Address"
                }),
            'city': TextInput(
                attrs={
                    'name': 'city',
                    'placeholder': "City"
                }),
            'state': TextInput(
                attrs={
                    'name': 'state',
                    'placeholder': "State"
                }),
            'zip_code': TextInput(
                attrs={
                    'name': 'zip_code',
                    'placeholder': "Zip code"
                }),
            'phone_number': TextInput(
                attrs={
                    'name': 'phone_number',
                    'placeholder': "Phone number"
                }),

        }
