from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, ProductDetailView, ProductListView

# from . import views


app_name = CatalogConfig.name

urlpatterns = [
    # path("", views.home, name="home"),
    # path("contacts/", views.contacts, name="contacts"),
    # path("products_list/", views.products_list, name="products_list"),
    # path("products/<int:pk>/", views.products_detail, name="products_detail"),
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
