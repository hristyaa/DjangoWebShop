from django.http import HttpResponse
# from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Contact, Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')


class ContactsTemplateView(TemplateView):
    model = Contact
    template_name = "catalog/contacts.html"

    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            name = self.request.POST.get("name")
            message = self.request.POST.get("message")
            return HttpResponse(f'Спасибо, {name}! Сообщение: "{message}" получено.')


# def home(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     latest_products = Product.objects.all().order_by("-created_at")[:5]
#     print("Последние 5 созданных продуктов:")
#     for product in latest_products:
#         print(f"{product.name} - {product.price} руб.")
#     return render(request, "catalog/home.html", context)
#
#
# def contacts(request):
#     data = Contact.objects.all()
#     context = {"contacts": data}
#
#     if request.method == "POST":
#         name = request.POST.get("name")
#         message = request.POST.get("message")
#
#         return HttpResponse(f'Спасибо, {name}! Сообщение: "{message}" получено.')
#     return render(request, "catalog/contacts.html", context)
#
#
# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "catalog/products_list.html", context)
#
#
# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "catalog/product_detail.html", context)
