from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html', context={'user':{'name' : 'ivan', 'surname': 'Ivanov'}, 'arr': [1, 2, 3, 4, 5]})


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
#чисто для комитапше
