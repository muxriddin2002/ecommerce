from django.contrib import admin
from .models import Customer
from .forms import CustomerCreation,CustomerChange
from django.contrib.auth.admin import UserAdmin

class CustomerAdmin(UserAdmin):
    model = Customer
    add_form = CustomerCreation
    form = CustomerChange

    list_display = ['username','email','adress','phone_number','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('adress','phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('adress','phone_number')}),
    )



admin.site.register(Customer,CustomerAdmin)