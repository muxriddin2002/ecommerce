from django.shortcuts import render, redirect
from product.models import Product,Comment
from django.views.generic import DetailView
from .forms import Product_CommentForm
from order.models import Order, Wishlist
from main.views import dataCart,product_meneger


def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    form = Product_CommentForm
    userCart = dataCart(request)
    products = product_meneger()
    comments = Comment.objects.filter(product=product)
    # discount_products = Product.objects.filter(discount=not None)
    if request.user.is_authenticated:

        if request.POST:
            try:
                update_post = request.POST.copy()
                update_post.update({
                    'user': request.user,
                    'product': product
                })
                formPost = Product_CommentForm(update_post)
                formPost.save()
            except:
                print('Xatolik')

    else:
        order = {}
        wishlist = {}

    data = {
        'product': product,
        'form': form,
        'comments': comments,
        'discount_products': products['discounted'],
        'userCart': userCart
    }

    return render(request, 'products/product_detail.html', data)

