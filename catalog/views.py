from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm, ProductAdminForm
from catalog.models import Contact, Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return ProductAdminForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        else:
            return ProductForm

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return ProductAdminForm
        elif user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.request.user

        if not (user.is_superuser or user.has_perm('catalog.can_unpublish_product') or user == self.object.owner):
            return HttpResponseForbidden('У вас нет прав на редактирование продукта.')

        return super().post(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        user = self.request.user
        is_moderator = user.groups.filter(name='Модератор продуктов').exists()

        if not (product.owner == user or user.is_superuser or (user.has_perm('catalog.delete_product') and is_moderator)):
            return HttpResponseForbidden('У вас нет прав на удаление продукта.')

        product.delete()

        return redirect('catalog:products_list')


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
