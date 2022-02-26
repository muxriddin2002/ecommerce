from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomerCreation
from django.urls import reverse_lazy
from order.models import *
from main import views as main_views



def loginPage(request):
    userCart = main_views.dataCart(request)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('home')

        else:
            messages.error(request, "Login yoki parol noto'g'ri")

    return render(request, 'registration/login.html', {'userCart': userCart})




def register(request):
    userCart = main_views.dataCart(request)
    form = CustomerCreation()
    if request.method == 'POST':
        formPost = CustomerCreation(request.POST)
        if formPost.is_valid():
            formPost.save()
            messages.success(request, "Ro'yhatdan o'tish muvaffaqiytali bajarildi!")

            return redirect('login')

        else:
            error = formPost._errors
            messages.error(request, str(error))

    data = {'form': form, 'userCart': userCart}
    return render(request, 'registration/signup.html', data)


def profile(request):
    if request.user.is_authenticated:
        try:
            orders = Order.objects.filter(customer=request.user, ordered=True)[::-1]
        except:
            orders = {}
    else:
        orders = {}

    return render(request,'customer/profile.html',{'orders':orders})




