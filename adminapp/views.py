from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ProductForm, DiscountForm, CategoryForm
from product.models import Product, Category, Discount
import json

def login_admin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('admin-home')

            else:
                messages.error(request, "Login yoki parol noto'g'ri")
        else:
            messages.error(request, "Login yoki parol noto'g'ri")

    return render(request, 'adminapp/registration/admin_login.html', {})

def admin_homePage(request):
    return render(request, 'adminapp/index.html', {})


def discount_admin(request):
    discount = Discount.objects.all()

    data = {
        'discount': discount
    }
    return render(request, 'adminapp/discount_admin/discountList.html', data)

def discount_create(request):
    form = DiscountForm

    if request.POST:
        formPost = form(request.POST)
        if formPost.is_valid():
            formPost.save()
            return redirect('discount-list')

    data = {
        'form': form
    }

    return render(request, 'adminapp/models/form.html', data)

def discount_update(request,pk):
    model = Discount.objects.get(id=pk)
    form = DiscountForm(request.POST or None,instance=model)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('discount-list')


    data = {
        'model': model,
        'form': form
    }
    return render(request, 'adminapp/models/form.html', data)

def category_admin(request):
    category = Category.objects.all()
    data = {
        'category': category
    }

    return render(request, 'adminapp/category/category_list.html', data)


def category_update(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=category)

    data = {
        'model': category,
        'form': form
    }
    return render(request, 'adminapp/models/form.html', data)

def category_create(request):
    form = CategoryForm
    data = {
        'form': form
    }
    return render(request, 'adminapp/models/form.html', data)


def product_admin(request):
    products = Product.objects.all().order_by('-date')

    data = {

        'products': products
    }

    return render(request, 'adminapp/model/list.html', data)

def product_create(request):
    form = ProductForm
    data = {
        'form': form
    }
    return render(request, 'adminapp/model/form.html', data)

def product_update(request,pk):
    model = Product.objects.get(id=pk)

    form = ProductForm(request.POST or None, instance=model)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product-admin-list')

    data = {
        'form': form,
        'model': model
    }
        
    return render(request, 'adminapp/model/form.html', data)

def product_delete(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    product = Product.objects.get(id=product_id)

    product.delete(using=None, keep_parents=False)

    return JsonResponse(f"Item o'chirildi-{product}", safe=False)


