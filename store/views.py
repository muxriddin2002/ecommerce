import json

from django.shortcuts import render
from product.models import Product, Category
from main.views import dataCart, product_meneger


def filter(request):
    all_products = product_meneger()['notebooks']
    products = product_meneger()['notebooks']
    userCart = dataCart(request)
    category_all = Category.objects.all()
    parents, category, base_category = [], [], []
    brands = {}
    for i in category_all:
        parents.append(i.parent)
    for i in category_all:
        if i not in parents:
            category.append(i)

    for i in category:
        brands[i] = len(Product.objects.filter(category=i))
    base_category = Category.objects.filter(parent=None)
    


    # if request.GET:
    #     result = []
    #     for i in brands:
    #         if request.GET.get(str(i)):
    #             for x in Product.objects.filter(category=i):
    #                 result.append(x)
    #
    #     products = result



    data = {
        'all_products': all_products,
        'products': products,
        'userCart': userCart,
        'brands': brands,
        'category': base_category
    }
    return render(request, 'filter/filter.html', data)

def filter_result(request):
    data = json.loads(request.body)



def search(request):
    userCart = dataCart(request)
    if request.GET:
        value = request.GET.get('search-product-name')
        result1 = Product.objects.filter(name__icontains=value)
        result2 = Product.objects.filter(category__name__icontains=value)
        result = []
        result.extend(result1)
        result.extend(result2)
        print(result)



    else:
        result = {}


    return render(request, 'filter/search.html', {'products': result, 'userCart':userCart})