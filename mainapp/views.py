from django.shortcuts import render
from .models import Product

def main(request):
    product_list = Product.objects.all()
    return render(request, 'mainapp/index.html', context={'user': request.user , 'products': product_list})


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')

