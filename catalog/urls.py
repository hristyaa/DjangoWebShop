from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import *

# from . import views


app_name = CatalogConfig.name

urlpatterns = [
    # path("", views.home, name="home"),
    # path("contacts/", views.contacts, name="contacts"),
    # path("products_list/", views.products_list, name="products_list"),
    # path("products/<int:pk>/", views.products_detail, name="products_detail"),
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("products/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
