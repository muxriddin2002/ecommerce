import json
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from product.models import Product
from .models import Order,Order_Item,Wishlist,Shipping_Adress
from .foms import Shipping_AdressForm
from customer.models import Customer
from django.http import JsonResponse
from datetime import datetime
from main.views import dataCart

def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    product = Product.objects.get(id=product_id)
    count = int(data['count'])
    userCart = dataCart(request)
    if request.user.is_authenticated:
        order = userCart['order']
        if count > product.quantity:
            count = product.quantity

        order.add_to_order(product_id, count)
    return JsonResponse("Cartaga qo'shildi", safe=False)


def checked(request):

    return render(request, 'order/checked.html')


def check_process(request):
    order, created = Order.objects.get_or_create(customer=request.user, ordered=False)
    data = json.loads(request.body)
    userCart = dataCart(request)
    order = userCart['order']



    if request.user.is_authenticated and order.get_total_price > 0:
        if request.POST:
            formPost = Shipping_AdressForm(request.POST)
            if formPost.is_valid():
                pass

        shipping_adress = Shipping_Adress.objects.create(
            order=order,
            customer=request.user,
            adress=data['shipping']['adress'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zip_code=data['shipping']['zip_code'],
            phone_number=data['shipping']['phone_number']
        )

        order.ordered = True
        order.date_complete = str(datetime.now())
        order.save()
        items = order.get_items()

        for item in items:
            item.product.quantity -= item.quantity
            item.product.save()

        return JsonResponse('true', safe=False)
    else:
        return JsonResponse('false', safe=False)

def update_cart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    product = Product.objects.get(id=product_id)
    action = data['action']

    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        if action == 'add':
            order, created = Order.objects.get_or_create(customer=request.user, ordered=False)
            try:
                item = Order_Item.objects.get(product=product, order=order)
                if product.quantity > 0 and item.quantity < product.quantity:
                    order.add_to_order(product_id)
            except:
                if product.quantity > 0:
                    order.add_to_order(product_id)


        elif action == 'remove':
            order = Order.objects.get(customer=request.user,ordered=False)
            order.remove_from_order(product_id)

    else:
        print("saytga login qilinmagan!")


    return JsonResponse(f'Jsonresponse --- Product_id: {product_id}, action: {action}', safe=False)








def remove_from_cart(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    order = Order.objects.get(customer=request.user,ordered=False)
    item = Order_Item.objects.get(id=item_id)
    print(item)

    print(order)

    item.delete(using=None,keep_parents=False)
    order.save()

    return JsonResponse(f"Item o'chirildi-{item_id}",safe=False)



def update_wishlist(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        if action == 'add':
            wishlist_cart, created = Wishlist.objects.get_or_create(customer=request.user)
            wishlist_cart.products.add(product)
            wishlist_cart.save()

        elif action == 'remove':
            wishlist_cart = Wishlist.objects.get(customer=request.user)
            wishlist_cart.products.remove(product)
            wishlist_cart.save()


    else:
        print('Foydalanuchi topilmadi')

    return JsonResponse(f'Tanlangan tovarlar, action:{action}, product id:{product_id}',safe=False)

