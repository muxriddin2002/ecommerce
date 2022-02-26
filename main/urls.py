
from django.urls import path
from . import views
from store import views as store_views
from order.views import update_cart,remove_from_cart,update_wishlist,check_process,add_to_cart
from product.views import product_detail
from customer.views import register, profile,loginPage
urlpatterns = [

    path('', views.index, name='home'),
    path('cart', views.order_cart, name='cart'),
    path('wishlist', views.wishlist, name='wishlist'),

    path('product-detail/<int:pk>', product_detail, name='product-detail'),

    path('signup', register, name='signup'),
    path('profile', profile, name='profile'),
    path('login/', loginPage, name='login'),


    path('update_cart/', update_cart, name='update_cart'),
    path('remove_from_cart/', remove_from_cart, name="remove_from_cart"),
    path('update_wishlist/', update_wishlist,name='update_wishlist'),

    path('add-to-cart/', add_to_cart, name='add-to-cart'),

    path('checkout', views.checkout, name='checkout'),
    path('check_process/', check_process, name='check_process'),

    path('filter/', store_views.filter, name='filter'),
    path('search/', store_views.search, name='search')
]
