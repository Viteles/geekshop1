from django.shortcuts import render, get_object_or_404
from .models import ProductCategory
from .models import Product

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

    same_products = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket,

    }

    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')


