from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def get_hot_product():
    return Product.objects.all().first()


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    product_list = Product.objects.all()

    return render(request, 'mainapp/index.html', context={'user': request.user , 'products': product_list})


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    # basket = request.user.basket.all()[0] if request.user.is_authenticated else []

    if pk:
        if pk == '0':
            category = {'name': 'Все'}
            product_list = Product.objects.all()
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category=category.id)

        context = {
            'title': 'Продукты',
            'links_menu': links_menu,
            'products': product_list,
            'category': category,
        }
        return render(request, 'mainapp/product_list.html', context)
    else:
        product_list = Product.objects.all()

        hot_product = get_hot_product()
        same_products = get_same_products(hot_product)

        context = {
            'title': 'Продукты',
            'links_menu': links_menu,
            'hot_product': hot_product,
            'same_products': same_products,
        }
        return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'Продукт'

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')

