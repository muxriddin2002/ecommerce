from django.urls import path
from .import views
urlpatterns = [
    path('', views.login_admin, name='admin-login'),
    path('home/', views.admin_homePage, name='admin-home'),
    path('product/list/', views.product_admin, name='product-admin-list'),
    path('product/add/', views.product_create, name='product-create'),
    path('product/edit/<int:pk>', views.product_update, name='product-update'),
    # path('product/delete/<int:pk>', views.product_delete, name='product-delete'),
    path('product-delete/', views.product_delete, name='product-delete'),

    path('category/list/', views.category_admin, name='category-list'),
    path('category/add/', views.category_create, name='category-create'),
    path('category/edit/<int:pk>', views.category_update, name='category-update'),

    path('discount/list/', views.discount_admin, name='discount-list'),
    path('discount/add/', views.discount_create, name='discount-create'),
    path('discount/edit/<int:pk>', views.discount_update, name='discount-update'),
    # path('discount/edit/<int:pk>', views.discount_delete, name='discount-delete')

]

