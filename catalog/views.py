from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Contact, Category


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    print("Последние 5 созданных продуктов:")
    for product in latest_products:
        print(f'{product.name} - {product.price} руб.')
    return render(request, 'catalog/home.html', context)


def contacts(request):
    data = Contact.objects.all()
    context = {'contacts': data}

    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')


        return HttpResponse(f'Спасибо, {name}! Сообщение: "{message}" получено.')
    return render(request, 'catalog/contacts.html', context)


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/products_list.html', context)



def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/products_detail.html', context)