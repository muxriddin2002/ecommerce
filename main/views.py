from django.shortcuts import render
from product.models import Product,Category,Discount,Notebook
from store.models import Slider,Banner
from order.models import Order,Order_Item,Wishlist
from order.foms import Shipping_AdressForm
import json
from django.http import HttpResponse


def error404(request, exception):
    return render(request, 'error_page/error_404.html', status=404)

def product_meneger():
    new_products = Product.objects.all()[:10]
    featured_products = new_products[:4]
    discounts = Discount.objects.all()
    discounted = []
    for i in discounts:
        discounted.extend(i.products.all())

    try:
        noteebooks_category = Category.objects.filter(tree_id=Category.objects.get(name='Notebook').tree_id)
        laptops = Notebook.objects.filter(category__in=noteebooks_category)
    except:
        laptops = {}
    try:
        smartphone_category = Category.objects.filter(tree_id=Category.objects.get(name='Smartphone').tree_id)
        smartphones = Product.objects.filter(category__in=smartphone_category)
    except:
        smartphones = {}

    slider = Slider.objects.all().order_by('-id')[:3]


    data = {
        'new_products': new_products,
        'smartphones': smartphones,
        'notebooks': laptops,
        'discounted': discounted,
        'slider': slider,
        'featured_products': featured_products
    }

    return data

def dataCart(request):
    if request.user.is_authenticated:
        try:
            order, created = Order.objects.get_or_create(customer=request.user, ordered=False)
            items = order.get_items().order_by('-date_add')
            null_items = items.filter(product__quantity=0)
            for item in null_items:
                item.quantity = 0

            none_items = items.filter(quantity=0)
            for i in none_items:
                if i.product.quantity > 0:
                    i.quantity = 1
                    i.save()

            for item in items:
                if item.quantity > item.product.quantity:
                    item.quantity = item.product.quantity


        except:
            print('order da xatolik')
            order, items = {}, {}
        try:
            wishlist = Wishlist.objects.get(customer=request.user)
            selected = wishlist.products.all()
        except:
            wishlist, selected = {}, {}
            # wishlist topilmadi
    else:
        order = {}
        items = {}
        wishlist = {}
        selected = {}
    data = {
        'order': order,
        'items': items,
        'wishlist': wishlist,
        'selected': selected
    }
    return data



def index(request):
    userCart = dataCart(request)
    products = product_meneger()
    data = {'products': products, 'userCart': userCart}
    return render(request,'main/home.html', data)


def checkout(request):
    form = Shipping_AdressForm
    userCart = dataCart(request)
    data = {'userCart': userCart, 'form': form}
    return render(request, 'order/checkout.html', data)



def wishlist(request):
    userCart = dataCart(request)
    data = {'userCart': userCart}
    return render(request, 'order/wishlist.html', data)

def order_cart(request):

    userCart = dataCart(request)
    data = {'userCart': userCart}


    return render(request, 'order/cart.html', data)

