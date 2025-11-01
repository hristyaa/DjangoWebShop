from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    print("Последние 5 созданных продуктов:")
    for product in latest_products:
        print(f'{product.name} - {product.price} руб.')
    return render(request, 'catalog/home.html')


def contacts(request):
    data = Contact.objects.all()
    context = {'contacts': data}

    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')


        return HttpResponse(f'Спасибо, {name}! Сообщение: "{message}" получено.')
    return render(request, 'catalog/contacts.html', context)


def index(request):
    return render(request, 'catalog/base.html')