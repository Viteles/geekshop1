from django.shortcuts import render, get_object_or_404
from .models import ProductCategory
from .models import Product
import random


def get_hot_product():
    return Product.objects.all().order_by('?').first()

def get_hot_product_from_admin():
    hot_products = Product.objects.filter(is_hot=True)
    if hot_products:
        hot_product = hot_products[0]
    else:
        hot_product = Product.objects.first()
    return hot_product


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    product_list = Product.objects.all()
    return render(request, 'mainapp/index.html', context={'user': request.user , 'products': product_list})


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = request.user.basket.all()
    if pk is not None:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,

        }

        return render(request, 'mainapp/products_list.html', context)

    else:
        hot_product = get_hot_product()
        same_products = get_same_products(hot_product)
        context = {
            'title': title,
            'links_menu': links_menu,
            'hot_product': hot_product,
            'same_products': same_products,
            'basket': basket,
        }


    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукты'
    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': request.user.basket.all(),
    }

    return render(request, 'mainapp/product.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')


